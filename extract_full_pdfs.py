import os
import re
from pypdf import PdfReader

pdf_mappings = {
    1: ['BLOCK 1.pdf', 'Unit-1.pdf'],
    2: ['MANI-002B3E.pdf'],
    3: ['MAN-002B5E.pdf', 'Unit-4 (1).pdf', 'Unit-8.pdf'],
    4: ['residence-and-kinship.pdf', 'Unit-3.pdf', 'Unit-5.pdf', 'BLOCK 2.pdf', 'Unit-1 (1).pdf', 'Unit7.pdf'],
    5: ['MANE-001-B1.pdf', 'Unit--3.pdf', 'Unit-11.pdf', 'Unit-2.pdf'],
    6: ['112.pdf', 'Block-3.pdf'],
    9: ['Unit-1 (2).pdf'],
    10: ['Block-4.pdf']
}

INPUT_FOLDER = r'C:\Users\ashis\Downloads\Folder_1'

def clean_paragraph(raw_text):
    lines = raw_text.split('\n')
    cleaned_lines = []
    
    skip_phrases = [
        "indira gandhi", "national open university", "course coordinator", 
        "block preparation", "print production", "all rights reserved",
        "isbn-", "check your progress", "suggested reading", "references",
        "let us sum up", "glossary", "sample questions", "learning objectives",
        "soss, ignou", "expert committee", "page "
    ]
    
    is_skipping_section = False
    
    for line in lines:
        line = line.strip()
        if not line or line.isdigit():
            continue
            
        lower_line = line.lower()
        
        # Stop at references or glossary
        if lower_line.startswith("references") or lower_line.startswith("suggested reading") or lower_line.startswith("glossary") or lower_line.startswith("let us sum up"):
            is_skipping_section = True
            continue
            
        if is_skipping_section:
            if re.match(r'^(unit \d+|block \d+|chapter \d+)$', lower_line) or lower_line.isupper() and len(lower_line) > 10:
                is_skipping_section = False # Might be a new section/unit starting
            else:
                continue

        if any(skip in lower_line for skip in skip_phrases) and len(line) < 100:
            continue
            
        cleaned_lines.append(line)
        
    # Re-join and fix line breaks
    joined = " ".join(cleaned_lines)
    
    # Split back into paragraphs heuristically based on long spaces or sentence ends
    joined = re.sub(r'([.?!])\s+([A-Z])', r'\1\n\n\2', joined)
    joined = re.sub(r'\s{3,}', '\n\n', joined)
    
    # Identify headers in the joined text (all caps usually)
    final_paras = []
    for para in joined.split('\n\n'):
        para = para.strip()
        if not para:
            continue
        if len(para) < 100 and (para.isupper() or para.istitle()):
            final_paras.append(f"\n### {para}\n")
        else:
            # Random pypdf artifacts like /head2right
            para = para.replace('/head2right', '- ')
            final_paras.append(para)
            
    return "\n\n".join(final_paras)

for unit_num, pdf_files in pdf_mappings.items():
    print(f"Processing Unit {unit_num} PDFs...")
    all_unit_text = f"\n\n## \ud83d\udcc4 Detailed PDF Content (Smart Reduced)\n\n"
    
    for pdf_name in pdf_files:
        pdf_path = os.path.join(INPUT_FOLDER, pdf_name)
        if not os.path.exists(pdf_path):
            continue
            
        print(f"  Reading {pdf_name}...")
        try:
            reader = PdfReader(pdf_path)
        except Exception as e:
            print(f"  Error reading {pdf_name}: {e}")
            continue
            
        all_unit_text += f"\n\n<details open>\n<summary><b>\ud83d\udcd6 Source Documents: {pdf_name}</b></summary>\n\n"
        
        pdf_text_parts = []
        # Process every page
        for page in reader.pages:
            t = page.extract_text()
            if t:
                pdf_text_parts.append(t + "\n")
        pdf_text_raw = "".join(pdf_text_parts)
                
        # Heuristic 20-30% reduction by dropping fluff and formatting
        smart_reduced_text = clean_paragraph(pdf_text_raw)
        
        # If it's too massive, we might want to trim or just let it be. 
        # The user specifically requested "actual content" with "smart reduction".
        all_unit_text += smart_reduced_text
        all_unit_text += "\n</details>\n"
        
    # Write to the unit's Summary.md
    summary_path = rf"C:\Users\ashis\Downloads\UGC_NET_Anthropology\Unit_{unit_num}\Summary.md"
    if os.path.exists(summary_path):
        # Replace surrogates before writing
        safe_text = all_unit_text.encode('utf-8', 'replace').decode('utf-8')
        with open(summary_path, 'a', encoding='utf-8') as f:
            f.write(safe_text)
            
print("PDF content successfully extracted and appended to markdown files.")
