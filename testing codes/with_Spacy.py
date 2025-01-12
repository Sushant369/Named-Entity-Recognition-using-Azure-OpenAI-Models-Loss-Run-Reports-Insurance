import fitz  # PyMuPDF
import spacy

# Load spaCy's NER model
nlp = spacy.load("en_core_web_sm")

# Path to the Loss Run Report PDF
pdf_path = "loss_run_report.pdf"

# Extract text from PDF
extracted_text = ""
with fitz.open(pdf_path) as pdf:
    for page in pdf:
        extracted_text += page.get_text()

# Save the extracted text for debugging
with open("extracted_text.txt", "w") as f:
    f.write(extracted_text)

print("Extracted Text:")
print(extracted_text)

# Apply NER to the extracted text
doc = nlp(extracted_text)

# Print the recognized entities
print("\nEntities found:")
for ent in doc.ents:
    print(f"{ent.text} | Start: {ent.start_char}, End: {ent.end_char} | Label: {ent.label_}")


import pandas as pd

# Organize entities into a DataFrame
data = {"Entity": [ent.text for ent in doc.ents],
        "Label": [ent.label_ for ent in doc.ents],
        "Start": [ent.start_char for ent in doc.ents],
        "End": [ent.end_char for ent in doc.ents]}

df = pd.DataFrame(data)

print("\nExtracted Entities:")
print(df)

# Filter for specific entity types
print("\nMonetary Values:")
print(df[df["Label"] == "MONEY"])

print("\nDates:")
print(df[df["Label"] == "DATE"])
