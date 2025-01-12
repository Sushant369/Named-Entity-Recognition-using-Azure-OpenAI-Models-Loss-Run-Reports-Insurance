from openai import AzureOpenAI
import os
from src.utils import load_keys, extract_text_from_pdf
openai_api_key = load_keys()["openai"]
openai_endpoint = load_keys()["endpoint"]

response = AzureOpenAI.Completion.create(
    engine="gpt-4o-mini",  # Replace with your actual deployment name
    prompt="Hello, world!",
    max_tokens=5
)
print(response)
