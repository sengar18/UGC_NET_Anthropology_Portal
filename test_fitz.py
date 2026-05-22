import fitz
import re

pdf_path = r'C:\Users\ashis\Downloads\Folder_1\MANI-002B3E.pdf'
doc = fitz.open(pdf_path)

skip_keywords = ["course coordinator", "block preparation", "print production", "all rights reserved",
                 "isbn-", "check your progress", "suggested reading", "references",
                 "let us sum up", "glossary", "expert committee", "indira gandhi national open university",
                 "school of social sciences", "programme coordinator"]

clean_text = []
skip_mode = False

for page in doc:
    blocks = page.get_text("blocks")
    for b in blocks:
        if b[6] != 0: # Ignore non-text (images)
            continue
            
        text = b[4].strip()
        if not text:
            continue
            
        text_lower = text.lower()
        
        # Heuristics to stop capturing irrelevant end-sections
        if text_lower == "references" or text_lower == "suggested reading" or text_lower == "let us sum up":
            skip_mode = True
            continue
            
        if re.match(r'^(unit \d+|block \d+|chapter \d+)$', text_lower):
            skip_mode = False # Reset if a new unit starts
            
        if skip_mode:
            continue
            
        # Ignore very short lines that might be page numbers or headers
        if len(text) < 15 and (text.isdigit() or text.isupper()):
            continue
            
        if any(sk in text_lower for sk in skip_keywords):
            continue
            
        # Ignore lines filled with "Dr. X" or "Professor Y" which IGNOU litters
        if "professor" in text_lower or "dr." in text_lower or "department of" in text_lower or "university" in text_lower:
            if len(text) < 150: # Usually these are short list items
                continue
                
        # Address line breaks within paragraphs
        para = text.replace('\n', ' ')
        para = re.sub(r'\s+', ' ', para).strip()
        
        # Add as a markdown paragraph
        if len(para) > 30: # Only decent sized paragraphs
            clean_text.append(para)

print("\n\n".join(clean_text[:15]))
