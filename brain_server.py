import json
import os
import sys
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
import unicodedata
import subprocess

def ensure_package(package, import_name):
    try:
        __import__(import_name)
    except ImportError:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to install {package}:\n{result.stderr}")
        __import__(import_name)

ensure_package("pymupdf", "fitz")
ensure_package("groq", "groq")

import fitz
from groq import Groq

def safe_path(filepath, base_dir):
    real = os.path.realpath(filepath)
    base = os.path.realpath(base_dir)
    if not real.startswith(base + os.sep):
        raise ValueError(f"Path escape blocked: {filepath}")
    return real

def sanitise(text, max_len=400):
    text = text[:max_len]
    text = "".join(c for c in text if unicodedata.category(c)[0] != "C")
    text = re.sub(r"(?i)(ignore|disregard|forget).{0,30}(above|previous|instruction)", "[redacted]", text)
    return text.strip()

# Read Groq API key securely from a local file to prevent GitHub Secret leaks
GROQ_API_KEY = ""
if os.path.exists("groq_key.txt"):
    with open("groq_key.txt", "r") as f:
        GROQ_API_KEY = f.read().strip()
else:
    print("\n[WARNING] groq_key.txt not found. AI Summarizer will be disabled, but Offline Textbook Scanner will still work!")

# Only initialize Groq client if key is present
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

CHUNKS_INDEX = []
from collections import defaultdict
INVERTED_INDEX: dict = defaultdict(list)

# --- 1. RECURSIVE MULTI-DIRECTORY SCANNER (PDF, MD, TXT) ---
def get_target_dirs():
    # Directories to scan recursively
    target_dirs = ["books", "notes"]
    # Also add Unit_1 to Unit_10 dynamically if they exist
    for i in range(1, 11):
        unit_dir = f"Unit_{i}"
        if os.path.exists(unit_dir):
            target_dirs.append(unit_dir)
    return target_dirs

def _process_pdf_file(filepath, base_dir, rel_path):
    chunks = []
    try:
        filepath = safe_path(filepath, base_dir)
        doc = fitz.open(filepath)
        buffer, start_page = "", 1
        for p in range(min(150, len(doc))):
            for block in doc[p].get_text("blocks"):
                if block[6] != 0: continue
                para = block[4].strip()
                if not para: continue
                if len(buffer) + len(para) > 1200:
                    if buffer:
                        chunks.append({"source": rel_path, "page": start_page, "text": buffer})
                    buffer = buffer[-150:] + " " + para
                    start_page = p + 1
                else:
                    buffer += (" " if buffer else "") + para
        if buffer:
            chunks.append({"source": rel_path, "page": start_page, "text": buffer})
        doc.close()
    except Exception as e:
        print(f"Error reading PDF {rel_path}: {e}")
    return chunks

def _process_text_file(filepath, base_dir, rel_path):
    chunks = []
    try:
        filepath = safe_path(filepath, base_dir)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().strip()
            if content:
                # Split large note files into 1000-char chunks for clean retrieval
                chunk_size = 1200
                overlap = 200
                start = 0
                chunk_idx = 1
                while start < len(content):
                    end = min(start + chunk_size, len(content))
                    chunks.append({
                        "source": f"{rel_path} (Chunk {chunk_idx})",
                        "page": None,
                        "text": content[start:end]
                    })
                    start += chunk_size - overlap
                    chunk_idx += 1
    except Exception as e:
        print(f"    Error reading notes {rel_path}: {e}")
    return chunks

def index_all_knowledge_assets():
    global CHUNKS_INDEX
    print("\n[Brain-Server] Scanning and indexing all books, notes, and unit files...")
    CHUNKS_INDEX = []

    target_dirs = get_target_dirs()

    for base_dir in target_dirs:
        if not os.path.exists(base_dir):
            continue
        print(f"  Scanning directory: {base_dir}...")
        
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath)
                
                # A. Handle PDF books/files
                if file.endswith('.pdf'):
                    CHUNKS_INDEX.extend(_process_pdf_file(filepath, base_dir, rel_path))
                
                # B. Handle Markdown or Text Notes
                elif file.endswith(('.md', '.txt')):
                    CHUNKS_INDEX.extend(_process_text_file(filepath, base_dir, rel_path))

    print(f"[Brain-Server] Successfully compiled {len(CHUNKS_INDEX)} page-level knowledge indexes!")
    build_inverted_index()

WORD_REGEX = re.compile(r'\b[a-zA-Z]{4,}\b')

def build_inverted_index():
    INVERTED_INDEX.clear()
    for idx, chunk in enumerate(CHUNKS_INDEX):
        for word in WORD_REGEX.findall(chunk["text"].lower()):
            INVERTED_INDEX[word].append(idx)

# --- 2. LOCAL VERBATIM KEYWORD MATCHER ---
def search_local_textbooks(question, doubt, top_n=3):
    stopwords = {'what','which','does','have','the','and','for','are','that'}
    q_words = set(WORD_REGEX.findall(question.lower())) - stopwords
    d_words = set(WORD_REGEX.findall(doubt.lower())) - stopwords
    scores = defaultdict(float)
    for w in q_words:
        for idx in INVERTED_INDEX.get(w, []):
            scores[idx] += 1.0
    for w in d_words:
        for idx in INVERTED_INDEX.get(w, []):
            scores[idx] += 5.0
    top = sorted(scores, key=scores.__getitem__, reverse=True)[:top_n]
    return [{"source": CHUNKS_INDEX[i]["source"], "page": CHUNKS_INDEX[i]["page"],
             "text": CHUNKS_INDEX[i]["text"]} for i in top]

# --- 3. LOCAL API SERVER HANDLER ---
class BrainRequestHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        ALLOWED_ORIGINS = {"http://localhost:3000"}
        origin = self.headers.get("Origin", "")
        if origin in ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/audit':
            content_length = int(self.headers['Content-Length'])

            if content_length > 1024 * 1024: # 1MB limit to prevent DoS
                self.send_response(413)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": "Payload Too Large"}).encode('utf-8'))
                return

            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                question = sanitise(data.get('question', ''))
                options = data.get('options', [])
                correct_answer = data.get('correct_answer', '')
                user_doubt = sanitise(data.get('user_doubt', ''))
                
                print(f"\n[Brain-Server] Challenge received for: '{question[:45]}...'")
                print(f"               Doubt: '{user_doubt}'")

                # 1. Run local offline verbatim search across books AND notes
                scanned_matches = search_local_textbooks(question, user_doubt, top_n=3)
                
                verbatim_block = "📖 VERBATIM TEXTBOOK & NOTES SCAN:\n\n"
                if scanned_matches:
                    for m in scanned_matches:
                        page_ref = f" (Page {m['page']})" if m['page'] else ""
                        verbatim_block += f"• From [{m['source']}]{page_ref}:\n"
                        verbatim_block += f"  \"{m['text']}\"\n\n"
                else:
                    verbatim_block += "  No matching note files or textbook pages found in index.\n\n"

                # 2. Try calling Groq AI Summarizer
                ai_summary = ""
                try:
                    context = "\n...\n".join([m['text'] for m in scanned_matches])
                    prompt = f"""You are a Senior Staff-Level Professor in Anthropology.
Analyse this question using the textbook and notes passages. Focus strictly on answering the USER DOUBT.

Source Passages:
{context}

Question Context: {question}
Currently Set Answer Key: {correct_answer}

USER DOUBT (PRIORITY): "{user_doubt}"

Write a concise 2-sentence resolution DIRECTLY ANSWERING the user's doubt. Cite the textbook names or note files to prove your point.
Resolution:"""
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": "You are a senior academic JRF Anthropology advisor."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.2,
                        max_tokens=250,
                    )
                    ai_summary = response.choices[0].message.content.strip()
                    print("[Brain-Server] AI summary generated successfully.")
                except Exception as api_err:
                    print(f"[Brain-Server] Groq API limit fallback triggered: {api_err}")
                    ai_summary = "⚠️ [API RATE LIMIT / OFFLINE MODE ACTIVE]\nGroq API free limit is active or offline. Displaying raw verbatim matched page content from your textbook library below."

                # Compile final output
                final_audit = f"{ai_summary}\n\n--------------------------------------------------\n{verbatim_block}"

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
                reply = {
                    "status": "success",
                    "audit_report": final_audit
                }
                self.wfile.write(json.dumps(reply).encode('utf-8'))

            except Exception as e:
                print(f"[Brain-Server] Error handling POST request: {e}")
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": "Internal Server Error"}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

# --- 4. START THE SERVER ---
def run_server(port=8001):
    index_all_knowledge_assets()
    server_address = ('', port)
    httpd = HTTPServer(server_address, BrainRequestHandler)
    print(f"\n=======================================================")
    print(f"  [BRAIN-SERVER] RECURSIVE HYBRID KNOWLEDGE ENGINE RUNNING!")
    print(f"  Listening on: http://localhost:{port}")
    print(f"  CORS Enabled | Auto-Indexes books/, notes/, & Unit_1-10")
    print(f"=======================================================\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Brain-Server] Shutting down...")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
