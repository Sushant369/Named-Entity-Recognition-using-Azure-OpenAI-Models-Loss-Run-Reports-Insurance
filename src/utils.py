import requests
import threading
import sys
import json
import os
import time
import pdfplumber
#import fitz  # PyMuPDF


def load_keys():
    f = open("Docs/keys.txt")
    k = "".join(f.readlines())
    keys = json.loads(k)
    f.close()
    return keys


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


#####################################################################
# # Path to the Loss Run Report PDF
# pdf_path = "Docs\Loss_Runs_Cincinnati_Amborn_Stone_LLC.pdf"

# # Extract text from PDF
# extracted_text = "" 
# with fitz.open(pdf_path) as pdf:
#     for page in pdf:
#         extracted_text += page.get_text()

# print(chain.run(extracted_text))
####################################################################