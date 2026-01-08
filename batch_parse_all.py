import os
from unstructured.partition.pdf import partition_pdf

input_folder = r"C:\Users\15007010\Desktop\Banas Chatbot\data"
output_folder = r"C:\Users\15007010\Desktop\Banas Chatbot\parsed_unstructured_fast"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        print(f"\n--- Parsing: {filename} (fast strategy) ---")
        
        # Use "fast" strategy - direct text extraction, no Poppler required
        elements = partition_pdf(
            filename=pdf_path,
            strategy="fast",            # Key change: fast & reliable for your docs
            languages=["eng"]
        )
        
        # Convert to clean Markdown-like text
        markdown_lines = []
        for element in elements:
            if hasattr(element, "text") and element.text:
                markdown_lines.append(element.text.strip())
        
        markdown_content = "\n\n".join(markdown_lines)
        
        print(f"Extracted content length: {len(markdown_content)} characters")
        
        if len(markdown_content.strip()) > 0:
            output_path = os.path.join(output_folder, filename.replace(".pdf", ".md"))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            print(f"Saved: {output_path}")
        else:
            print("Warning: Empty content extracted")



#Trying something new
print("\nAll done!")