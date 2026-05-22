from pypdf import PdfReader

pdf_path = r'C:\Users\ashis\Downloads\Folder_1\MANI-002B3E.pdf'
reader = PdfReader(pdf_path)

with open('test_extract.txt', 'w', encoding='utf-8') as f:
    for i in range(min(5, len(reader.pages))):
        f.write(f"--- PAGE {i} ---\n")
        f.write(reader.pages[i].extract_text() + "\n")
