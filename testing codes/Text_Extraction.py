import fitz  # PyMuPDF
import easyocr
import os
from PIL import Image

# Path to the PDF file
pdf_path = "Docs\S_&_A_FCCI_23_24_PKG_Loss_Runs.pdf"

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

# Extract pages and perform OCR
ocr_results = []
with fitz.open(pdf_path) as pdf:
    for page_num in range(len(pdf)):
        # Extract page as image
        pix = pdf[page_num].get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Perform OCR on the image
        text = reader.readtext(img, detail=0)
        text_combined = "\n".join(text)
        ocr_results.append(text_combined)

# Save the OCR results
output_dir = "ocr_output"
os.makedirs(output_dir, exist_ok=True)

# Save text results
for i, text in enumerate(ocr_results):
    with open(os.path.join(output_dir, f"page_{i + 1}.txt"), "w", encoding="utf-8") as f:
        f.write(text)

# Combine all text into a single file
with open("full_ocr_text.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(ocr_results))

print("OCR completed. Extracted text saved in 'ocr_output' directory.")
