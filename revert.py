import os

# Revert Summary.md files by removing the injected detailed PDF content
for unit_num in range(1, 11):
    summary_path = rf"C:\Users\ashis\Downloads\UGC_NET_Anthropology\Unit_{unit_num}\Summary.md"
    if os.path.exists(summary_path):
        with open(summary_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # The injected text starts with "## " followed by some characters and "Detailed PDF Content"
        # Since emojis might have rendered as ??, let's find the index of "Detailed PDF Content"
        idx = content.find("Detailed PDF Content")
        if idx != -1:
            # Find the start of the line with "## "
            start_idx = content.rfind("##", 0, idx)
            if start_idx != -1:
                clean_content = content[:start_idx].strip() + "\n"
                with open(summary_path, 'w', encoding='utf-8') as f:
                    f.write(clean_content)
                    
print("Reverted Summary.md files to remove messy text.")
