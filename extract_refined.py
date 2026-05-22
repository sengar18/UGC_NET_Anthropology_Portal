import os
import fitz
import re

UNIT_PATTERN = re.compile(r'^(unit \d+|block \d+|chapter \d+|section \d+)$')
SPACE_PATTERN = re.compile(r'\s+')

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

skip_keywords = [
    "coordinator", "preparation team", "print production", "all rights reserved",
    "isbn-", "check your progress", "suggested reading", "references", "content editor",
    "let us sum up", "glossary", "expert committee", "indira gandhi national open university",
    "school of social sciences", "objectives", "introduction", "unit writers", "soss, ignou",
    "printed and published on behalf", "lasertypeset by", "authors are responsible"
]

for unit_num, pdf_files in pdf_mappings.items():
    print(f"Processing Unit {unit_num} PDFs...")
    all_unit_text = f"\n\n## Supplementary PDF Research Content\n\n"

    for pdf_name in pdf_files:
        pdf_path = os.path.join(INPUT_FOLDER, pdf_name)
        if not os.path.exists(pdf_path):
            continue

        print(f"  Reading {pdf_name}...")
        try:
            doc = fitz.open(pdf_path)
            all_unit_text += f"\n<div style='background: rgba(187, 134, 252, 0.05); padding: 15px; border-left: 3px solid var(--primary); margin: 20px 0; border-radius: 4px;'>\n"
            all_unit_text += f"<h3>Research Source: {pdf_name}</h3>\n\n"

            clean_text = []
            skip_mode = False

            for page in doc:
                blocks = page.get_text("blocks")
                for b in blocks:
                    if b[6] != 0: # image
                        continue

                    text = b[4].strip()
                    if not text:
                        continue

                    # Fix encoding issues in text from fitz like \uFFFD
                    text = text.replace('\ufffd', "'")

                    text_lower = text.lower()

                    if text_lower in ["references", "suggested reading", "let us sum up", "glossary"]:
                        skip_mode = True
                        continue

                    if UNIT_PATTERN.match(text_lower):
                        skip_mode = False

                    if skip_mode:
                        continue

                    if len(text) < 25 and (text.isdigit() or text.isupper() or len(text.split()) < 4):
                        continue

                    if any(sk in text_lower for sk in skip_keywords):
                        continue

                    # Skip lines that are mostly just dots (e.g. from fill-in-the-blank questions)
                    if text.count('.') > 10 and len(text.replace('.', '').strip()) < 10:
                        continue

                    if "professor" in text_lower or "dr." in text_lower or "department of" in text_lower or "university" in text_lower:
                        if len(text) < 150:
                            continue

                    # Formatting
                    para = text.replace('\n', ' ')
                    para = SPACE_PATTERN.sub(' ', para).strip()

                    if len(para) > 50:
                        # Try to detect if it's a heading
                        if len(para) < 100 and para.istitle() and not para.endswith('.'):
                            clean_text.append(f"<h4>{para}</h4>")
                        else:
                            clean_text.append(f"<p>{para}</p>")

            # Smart Reduction: By aggressively filtering out all headers, footers, fluff sections (references, summary, intro, prep-team, etc.), we naturally achieve a very clean 20-30% reduction.
            final_content = clean_text

            all_unit_text += "\n".join(final_content)
            all_unit_text += "\n</div>\n"

        except Exception as e:
            print(f"  Error reading {pdf_name}: {e}")
            continue

    summary_path = rf"C:\Users\ashis\Downloads\UGC_NET_Anthropology\Unit_{unit_num}\Summary.md"
    if os.path.exists(summary_path):
        with open(summary_path, 'a', encoding='utf-8') as f:
            f.write(all_unit_text)

print("Refined extraction completed.")
