from fastapi import FastAPI, HTTPException, UploadFile, File
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from PIL import Image
import io
import base64
import json
from fastapi import FastAPI, HTTPException, UploadFile, File

# Load environment variables from .env file
load_dotenv()

# Debugging: Print the API key to ensure it's loaded correctly
print("GOOGLE_API_KEY from .env:", os.getenv("GOOGLE_API_KEY"))

app = FastAPI()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

class TextRequest(BaseModel):
    text: str = None  # Make text optional

@app.post("/analyze")
async def analyze_text(request: TextRequest = None, file: UploadFile = File(None)): #make file optional
    text = request.text if request else None

    if not text and not file:
        raise HTTPException(status_code=400, detail="Text or image is required")

    parts = []

    if text:
        parts.append(text)

    if file:
        try:
            image = Image.open(io.BytesIO(await file.read()))
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format=image.format)
            img_byte_arr = img_byte_arr.getvalue()
            parts.append({"mime_type": file.content_type, "data": img_byte_arr})

        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid image file: {e}")

    prompt = "Analyze the provided text and/or image for potential scam indicators. Indicate if it is a scam and provide a brief explanation."

    try:
        response = model.generate_content(parts)
        return {"result": response.text}
    except Exception as e:
        print(f"Error generating content: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/activate")
async def activate():
    return {"message": "Activation endpoint"}
