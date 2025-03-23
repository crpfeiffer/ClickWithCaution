import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List all available models
print("Available Models:")
for model in genai.list_models():
    print(f"Name: {model.name}")
    print(f"Description: {model.description}")
    print(f"Supported Methods: {model.supported_generation_methods}")
    print("-" * 40)