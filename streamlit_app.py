import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import re
import json

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
    base="light"
    primaryColor="#eef719"
    
    .reportview-container {
        background-color: white;
        color: #0E1117; /* Black font */
    }
    .stTextArea textarea {
        background-color: #f8f8f8;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        color: #0E1117; /* Black font */
    }
    .stButton button {
        background-color: #ffeb3b; /* Dark Yellow */
        color: #0E1117; /* Black font */
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }
    .stButton button:hover {
        background-color: #f9a825; /* Slightly darker yellow on hover */
    }
    .stAlert {
        background-color: #ffcdd2;
        color: #d32f2f;
        padding: 15px;
        border-radius: 5px;
    }
    .stSuccess {
        background-color: #c8e6c9;
        color: #388e3c;
        padding: 15px;
        border-radius: 5px;
    }
    .stHeader {
        color: #f9a825; /* Dark Yellow Header */
        text-align: center;
    }
    .result-container {
        background-color: #f0f0f0; /* Light Gray for result container */
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: #0E1117; /* Black font */
    }
    .scam-question {
        font-weight: bold;
        font-size: 18px;
        color: #f9a825; /* Dark Yellow Question */
    }
    .directions-container {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
        color: #0E1117; /* Black font for directions */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add logo (replace 'your_logo.png' with your logo file)
st.markdown("<div class='logo-container'><img = 'caution.png'></div>", unsafe_allow_html=True)

st.markdown("<h1 class='stHeader'>Click With Caution</h1>", unsafe_allow_html=True)

# Add directions
st.markdown("<div class='directions-container'><h3>Instructions:</h3><p>Enter the text you want to analyze in the text area below. Click 'Analyze' to check for potential scam indicators.</p></div>", unsafe_allow_html=True)

text = st.text_area("Enter text to analyze:")

if st.button("Analyze"):
    if not text:
        st.error("Please enter text to analyze.")
    else:
        prompt = f"""
        Analyze the following text for potential scam indicators: '{text}'. 
        Provide the output in the following JSON format:
        {{
            "is_scam": "Yes, it is likely a scam" or "No, not likely to be a scam",
            "confidence": (a number between 0 and 1 representing confidence),
            "explanation": "short explanation"
        }}
        """
        try:
            response = model.generate_content(prompt)
            result_text = response.text

            # Extract JSON from the response
            match = re.search(r'\{.*\}', result_text, re.DOTALL)
            if match:
                try:
                    result_json = json.loads(match.group(0))
                    st.markdown("<div class='result-container'>", unsafe_allow_html=True)
                    st.markdown(f"<span class='scam-question'>Is this a scam?</span> {result_json.get('is_scam', 'Unknown')}", unsafe_allow_html=True)
                    st.markdown(f"<span class='scam-question'>Confidence level out of 1.00:</span> {result_json.get('confidence', 'Unknown')}", unsafe_allow_html=True)
                    st.markdown(f"<span class='scam-question'>Explanation:</span> {result_json.get('explanation', 'No explanation provided')}", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                except json.JSONDecodeError:
                    st.error("Could not parse JSON from the response.")
                    st.write("Raw response:", result_text)
            else:
                st.error("Could not extract JSON from the response.")
                st.write("Raw response:", result_text)

        except Exception as e:
            st.error(f"An error occurred: {e}")