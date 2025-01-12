import spacy
from gliner_spacy.pipeline import GlinerSpacy
import fitz  # PyMuPDF

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("gliner_spacy",config={"labels": ["Policy Number", "Claims Number", "Incured"]})


# Path to the Loss Run Report PDF
pdf_path = "Docs\EMC_Package_loss_runs_for_United_Sport_Systems.pdf"

# Extract text from PDF
extracted_text = ""
with fitz.open(pdf_path) as pdf:
    for page in pdf:
        extracted_text += page.get_text()   

# # Save the extracted text for debugging
# with open("extracted_text.txt", "w") as f:
#     f.write(extracted_text)

# print("Extracted Text:")
# print(extracted_text)

# Apply NER to the extracted text
doc = nlp(extracted_text)

for ent in doc.ents:
    print(ent.text, ent.label)