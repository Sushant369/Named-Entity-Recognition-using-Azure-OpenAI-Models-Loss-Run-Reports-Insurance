from pdf2image import convert_from_path

# Convert PDF pages to images
pdf_path = "LOSSRUNREPORTS.pdf"
images = convert_from_path(pdf_path)

# Save the images as PNGs
for i, image in enumerate(images):
    image.save(f"page_{i+1}.png", "PNG")
