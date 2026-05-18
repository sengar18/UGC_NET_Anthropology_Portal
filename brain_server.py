import json
import os
import sys
import re
from http.server import HTTPServer, BaseHTTPRequestHandler

# Auto-install dependencies if missing
try:
    import fitz  # PyMuPDF
except ImportError:
    os.system(f"{sys.executable} -m pip install pymupdf")
    import fitz

try:
    from groq import Groq
except ImportError:
    os.system(f"{sys.executable} -m pip install groq")
    from groq import Groq

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

# --- 1. RECURSIVE MULTI-DIRECTORY SCANNER (PDF, MD, TXT) ---
def index_all_knowledge_assets():
    global CHUNKS_INDEX
    print("\n[Brain-Server] Scanning and indexing all books, notes, and unit files...")
    CHUNKS_INDEX = []

    # Directories to scan recursively
    target_dirs = ["books", "notes"]
    # Also add Unit_1 to Unit_10 dynamically if they exist
    for i in range(1, 11):
        unit_dir = f"Unit_{i}"
        if os.path.exists(unit_dir):
            target_dirs.append(unit_dir)

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
                    try:
                        doc = fitz.open(filepath)
                        pages_to_read = min(150, len(doc)) # index up to 150 pages for large books
                        for p in range(pages_to_read):
                            txt = doc[p].get_text().strip()
                            if txt:
                                CHUNKS_INDEX.append({
                                    "source": rel_path,
                                    "page": p + 1,
                                    "text": txt
                                })
                        doc.close()
                    except Exception as e:
                        print(f"    Error reading PDF {rel_path}: {e}")
                
                # B. Handle Markdown or Text Notes
                elif file.endswith(('.md', '.txt')):
                    try:
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
                                    CHUNKS_INDEX.append({
                                        "source": f"{rel_path} (Chunk {chunk_idx})",
                                        "page": None,
                                        "text": content[start:end]
                                    })
                                    start += chunk_size - overlap
                                    chunk_idx += 1
                    except Exception as e:
                        print(f"    Error reading notes {rel_path}: {e}")

    print(f"[Brain-Server] Successfully compiled {len(CHUNKS_INDEX)} page-level knowledge indexes!")

# --- 2. LOCAL VERBATIM KEYWORD MATCHER ---
def search_local_textbooks(query, top_n=3):
    # Strip common stopwords
    stopwords = {'what', 'which', 'who', 'does', 'really', 'have', 'the', 'and', 'for', 'are', 'there', 'that', 'should'}
    q_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', query.lower())) - stopwords
    
    scored = []
    for idx, page_data in enumerate(CHUNKS_INDEX):
        c_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', page_data['text'].lower()))
        score = len(q_words & c_words)
        
        # Boost matches for critical terms
        critical_terms = ['schedule', 'governor', 'neanderthal', 'equilibrium', 'malinowski', 'lineage', 'prehistory', 'chromosomal']
        for term in critical_terms:
            if term in query.lower() and term in page_data['text'].lower():
                score += 3
                
        if score > 0:
            scored.append((score, idx))
            
    scored.sort(reverse=True, key=lambda x: x[0])
    
    verbatim_results = []
    for score, idx in scored[:top_n]:
        match = CHUNKS_INDEX[idx]
        cleaned_text = re.sub(r'\n+', '\n', match['text'])
        if len(cleaned_text) > 400:
            cleaned_text = cleaned_text[:400] + "..."
            
        verbatim_results.append({
            "source": match['source'],
            "page": match['page'],
            "text": cleaned_text
        })
    return verbatim_results

# --- 3. LOCAL API SERVER HANDLER ---
class BrainRequestHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/audit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                question = data.get('question', '')
                options = data.get('options', [])
                correct_answer = data.get('correct_answer', '')
                user_doubt = data.get('user_doubt', '')
                
                print(f"\n[Brain-Server] Challenge received for: '{question[:45]}...'")
                print(f"               Doubt: '{user_doubt}'")

                # 1. Run local offline verbatim search across books AND notes
                scanned_matches = search_local_textbooks(question + " " + user_doubt, top_n=3)
                
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
Analyse this question doubt using the textbook and notes passages.
Source Passages:
{context}

Question: {question}
Options: {options}
Answer Key: {correct_answer}
User Doubt: "{user_doubt}"

Write a concise 2-sentence resolution verifying the facts. Cite the textbook names or note files.
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
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
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
