
from dotenv import load_dotenv


import os
import streamlit as st
import textwrap

import google.generativeai as genai
from IPython.display import Markdown

# Load environment variables from .env
load_dotenv()

# Configure the Google Gemini API
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("Google API key not found. Please check your .env file.")
else:
    genai.configure(api_key=API_KEY)

def to_markdown(text):
    # Convert bullet points to markdown format
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

## Function to load Gemini model and get response

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(question)
    return response.text


# Streamlit app configuration
st.set_page_config(page_title="generatetext")

# App title
st.header("Gemini LLM Application")

# Input text box
user_input = st.text_input("Type something:", key="input")

# Submit button
if st.button("Generate"):
    if user_input:
        # Get response from Gemini
        response = get_gemini_response(user_input)
        st.subheader("The Response:")
        st.write(response)
    else:
        st.error("Please enter a question.")
