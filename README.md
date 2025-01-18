# Named Entity Recognition Using Azure OpenAI Models for Loss Run Reports in Insurance

## Overview

This project demonstrates an automated solution for extracting structured information from insurance loss run reports using **Azure OpenAI Models**. It focuses on Named Entity Recognition (NER) tasks to identify policy details, claim information, and financial data, saving the results in structured formats like Excel for further analysis.

---

## Features

- **Automated Data Extraction**:
  - Extracts detailed policy and claim information from PDF loss run reports.
  - Uses Azure OpenAI's GPT models for high-accuracy NER tasks.

- **Schema-Driven Processing**:
  - Ensures consistent and validated outputs using a predefined JSON schema.

- **Custom Prompts**:
  - Utilizes a domain-specific custom prompt to extract relevant data.

- **Flexible Output**:
  - Saves the extracted data in structured formats like JSON and Excel.

- **Integration Ready**:
  - Built for seamless integration into insurance workflows.

---

## Installation

### Prerequisites

- **Python**: Version 3.8+
- **Packages**:
  - `langchain_community`
  - `langchain`
  - `dotenv`
  - `pandas`
  - `openai`
  - `langchain_openai`

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Sushant369/Named-Entity-Recognition-using-Azure-OpenAI-Models-Loss-Run-Reports-Insurance.git
   cd Named-Entity-Recognition-using-Azure-OpenAI-Models-Loss-Run-Reports-Insurance
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Azure OpenAI credentials:
   - Create a `.env` file in the project root with the following variables:
     ```env
     AZURE_OPENAI_KEY=<your-azure-openai-key>
     AZURE_OPENAI_ENDPOINT=<your-azure-openai-endpoint>
     ```

4. Organize input files:
   - Place PDF files in the `Docs` directory for processing.

---

## Usage

### Run the Script

1. Execute the main script:
   ```bash
   python main.py
   ```

2. The script will:
   - Extract text from the PDF.
   - Parse and structure the data using Azure OpenAI.
   - Save the results as an Excel file in the `output` directory.

---

## Project Structure

```
├── src/
│   ├── utils.py        # Utility functions for key management and PDF processing
├── Docs/               # Directory for input PDF files
├── output/             # Directory for output Excel files
├── .env                # Environment variables for credentials
├── main.py             # Main script for data extraction
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## Example Schema

The JSON schema ensures consistency and accuracy of the extracted data:

```json
{
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
}
```

---

## Outputs

1. **Console Logs**:
   - Logs intermediate steps for debugging and validation.

2. **Excel File**:
   - Extracted data is saved as an Excel file named after the input PDF in the `output` directory.

---

## How It Works

1. **Text Extraction**:
   - Extracts raw text from PDF files using a utility function.

2. **Prompt-based Data Parsing**:
   - Applies a custom prompt to extract structured data using Azure OpenAI.

3. **Validation and Structuring**:
   - Validates extracted entities against a predefined JSON schema.

4. **Output Generation**:
   - Saves the structured data in Excel format for easy analysis.

---

## Future Enhancements

- **Improved PDF Parsing**:
  - Enhance handling of complex table structures in PDFs.

- **Error Handling**:
  - Add robust error handling for unexpected input formats.

- **Visualization**:
  - Integrate basic data visualization for claims analysis.

---

## Contact

For inquiries or support, contact [Your Name] at [Your Email].
```

