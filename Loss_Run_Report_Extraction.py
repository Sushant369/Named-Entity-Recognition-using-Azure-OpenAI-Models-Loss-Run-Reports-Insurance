from langchain_community.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain
from src.utils import load_keys, extract_text_from_pdf
import os
from dotenv import load_dotenv
import pandas as pd
from langchain_openai import AzureChatOpenAI
from openai import AzureOpenAI
import langchain.chains.openai_functions

# Load environment variables
load_dotenv()
os.environ["AZURE_OPENAI_KEY"] = load_keys()["openai"]
os.environ["AZURE_OPENAI_ENDPOINT"] = load_keys()["endpoint"]

# Initialize Azure OpenAI LLM
llm = AzureChatOpenAI(
    azure_deployment="gpt-4o-mini-WBMI1",
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-06-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    temperature=0
)

# Extract Data from PDF
pdf_path = "Docs\ilovepdf_split-range\LOSSRUNREPORTS-14-15.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

# print("################################################################")

# print(extracted_text)
# print("################################################################")

# Define Schema
schema = {
    "properties": {
        "Policy Number": {"type": "string"},
        "Policy Type": {"type": "string"},
        "Policy Effective": {"type": "string", "format": "date"},
        "Policy Term": {"type": "string"},
        "Claim Number": {"type": "string"},
        "Claim Date": {"type": "string", "format": "date"},
        "Loss Type": {"type": "string"},
        "Description of Loss": {"type": "string"},
        "Location of Loss": {"type": "string"},
        "Loss Paid": {"type": "number"},
        "Expense Paid": {"type": "number"},
        "Medical Paid": {"type": "number"},
        "Total Incurred": {"type": "number"},
        "Claim Count": {"type": "number", "description": "Claim count for that particular policy term"},
        "Loss Year": {"type": "integer"},
        "Accident Date": {"type": "string", "format": "date"},
        "Resolution Time": {"type": "integer", "description": "Time in days to resolve the claim"}
    }
}

# Define Custom Prompt
custom_prompt = """
You are an AI tasked with extracting specific details from a loss run report. There can be multiple claims for same policies we need all the data. Dont use any extranal data except the text provided. Use the following instructions to extract the required information:

### Extraction Rules:
1. **Policy Details**:
   - Policy Number: The unique identifier of the policy.
   - Policy Type: The type of policy (e.g., Auto, Home, General Liability).
   - Policy Effective: The start date of the policy (in YYYY-MM-DD format). This can be different for claims.
   - Policy Term: The duration of the policy (e.g., 1 Year, 6 Months).

2. **Claim Details**:
   - Claim Number: The unique identifier for the claim.
   - Claim Date: The date the claim was filed (in YYYY-MM-DD format).
   - Loss Type: The category of loss (e.g., Fire, Theft, Collision).
   - Description of Loss: A brief description of what caused the loss.
   - Location of Loss: The physical location where the loss occurred.

3. **Financial Data**:
   - Loss Paid: The amount paid to cover the loss (numeric value).
   - Expense Paid: The amount paid for additional expenses (numeric value).
   - Medical Paid: The amount paid for medical costs (numeric value).
   - Total Incurred: The total amount incurred for the claim (numeric value).
   - Claim Count: The total number of claims made for that particular policy term.

4. **Time and Date Details**:
   - Loss Year: The year the loss occurred.
   - Accident Date: The date of the accident (in YYYY-MM-DD format).
   - Resolution Time: The time in days taken to resolve the claim.

### Output Format: 
Provide the extracted details in JSON format. For example:

{{
    "Policy Number": "123456789",
    "Policy Type": "Auto",
    "Policy Effective": "2023-01-01",
    "Policy Term": "1 Year",
    "Claim Number": "CLM12345",
    "Claim Date": "2023-06-15",
    "Loss Type": "Collision",
    "Description of Loss": "Rear-end collision on the highway.",
    "Location of Loss": "Houston, TX",
    "Loss Paid": 5000,
    "Expense Paid": 200,
    "Medical Paid": 1500,
    "Total Incurred": 6700,
    "Claim Count": 1,
    "Loss Year": 2023,
    "Accident Date": "2023-06-01",
    "Resolution Time": 14
}}
input text: {text}"""

# Adjust prompt application
formatted_prompt = custom_prompt.format(text=extracted_text)

# Run the LLM with the formatted prompt
response = llm(formatted_prompt)
# print(response.content)

# # Parse the JSON string
# import json
# if response.content.startswith("```json") and response.content.endswith("```"):
#     cleaned_content = response.content[7:-3]
# else:
#     cleaned_content = response.content.strip()
# print(cleaned_content)
# policy_data = json.loads(cleaned_content)


# # policy_data = json.loads(response.content.strip())

# # Extract policy-level and claims-level data
# policy_info = {k: v for k, v in policy_data.items() if k != "Claims"}
# claims_data = policy_data["Claims"]

# # # Add policy-level data to each claim
# for claim in claims_data:
#     claim.update(policy_info)

# # Convert claims to a DataFrame
# df = pd.DataFrame(claims_data)



# # print("################################################################")

# # print(response)
# # print("################################################################")


# Create Chain object
chain = create_extraction_chain(schema, llm)

# Run the chain to extract data
extracted_entities = chain.run(response)

# Validate and normalize extracted entities
if isinstance(extracted_entities, list):
    # Ensure all schema keys are present in the output
    schema_keys = list(schema["properties"].keys())
    normalized_data = [
        {key: entity.get(key, None) for key in schema_keys}
        for entity in extracted_entities
    ]

    # Create DataFrame
    df = pd.DataFrame(normalized_data, columns=schema_keys)
else:
    raise ValueError("Extracted entities are not in the expected format.")

# Print the DataFrame
print(df)

# # Save the DataFrame to an Excel file
file_name = pdf_path.split("\\")[-1].split(".")[0] + "_loss_run_report.xlsx"
df.to_excel(file_name, index=False)
print(f"Data successfully saved to {file_name}")
