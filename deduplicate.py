import os
import glob
import string
import re

def normalize_text(text):
    # Remove HTML tags for comparison
    text = re.sub(r'<[^>]+>', '', text)
    # Remove punctuation and lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

print("Starting cross-unit redundancy removal...")

seen_paragraphs = set()
redundancy_count = 0
total_removed_chars = 0

for file_path in sorted(glob.glob(r'C:\Users\ashis\Downloads\UGC_NET_Anthropology\Unit_*\Summary.md')):
    print(f"Processing {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Split content by double newlines to evaluate paragraphs/blocks
    blocks = content.split('\n\n')
    new_blocks = []
    
    for block in blocks:
        # Ignore structural elements, short lines, or code blocks
        if block.startswith('##') or block.startswith('#') or block.startswith('<div') or block.startswith('</div>') or block.startswith('<summary'):
            new_blocks.append(block)
            continue
            
        # For `<p>` tags or raw text, check if it's redundant
        norm = normalize_text(block)
        
        # Only check blocks that have substantial text (e.g. at least ~10 words)
        if len(norm.split()) < 10:
            new_blocks.append(block)
            continue
            
        if norm in seen_paragraphs:
            # We found a redundant paragraph!
            redundancy_count += 1
            total_removed_chars += len(block)
            # Skip appending it to new_blocks
        else:
            seen_paragraphs.add(norm)
            new_blocks.append(block)
            
    # Reassemble the file
    deduped_content = '\n\n'.join(new_blocks)
    
    # Clean up multiple empty lines that might have been created
    deduped_content = re.sub(r'\n{3,}', '\n\n', deduped_content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(deduped_content)

print(f"\nDone! Removed {redundancy_count} redundant paragraphs across all units.")
print(f"Total characters removed: {total_removed_chars}")
