from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from src.utils import load_keys
import os
import pdfplumber
import pandas as pd

# Load environment variables
os.environ["OPENAI_API_KEY"] = load_keys()["openai"]

# Initialize LLM
llm = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"], model='gpt-4o-mini')

# Extract text from PDF using pdfplumber
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

pdf_path = "Docs/Loss_Runs_Cincinnati_Amborn_Stone_LLC.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

# Define a detailed custom prompt
custom_prompt = f"""
You are a data extraction assistant. Extract all the claims from the given loss run report. 
The output should be in JSON format, where each claim has the following fields:
- Policy Number
- Claim Number
- Claim Date
- Loss Type
- Description of Loss
- Location of Loss
- Policy Term
- Loss Paid
- Expense Paid
- Loss Reserve
- Total Incurred

Ensure no claims are missed. Here is the report text:

{extracted_text}
"""

# Convert the prompt into a HumanMessage
messages = [HumanMessage(content=custom_prompt)]

# Use the LLM to generate a response
response = llm(messages)

# Process the LLM's response
try:
    extracted_entities = eval(response.content)  # Convert the JSON string to Python objects
    if isinstance(extracted_entities, list):
        df = pd.DataFrame(extracted_entities)
        print(df)
        df.to_excel("loss_run_report.xlsx", index=False)
    else:
        raise ValueError("Extracted entities are not in the expected format.")
except Exception as e:
    print(f"Error processing response: {e}")
