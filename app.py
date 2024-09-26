#Gemini flash model

from dotenv import load_dotenv
load_dotenv()  #take environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

#Configure the Gemini API with environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Gemini model and get response.
def get_gemini_response(input_text, image=None):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input_text and image:
        response = model.generate_content([input_text, image])
    elif input_text:
        response = model.generate_content([input_text])
    else:
        response = model.generate_content([image])
    return response.text

#Initialize Streamlit app
st.set_page_config(page_title="generatetext")

#Create two tabs
tab1, tab2 = st.tabs(["Text", "Text & Image"])

#Tab 1: text
with tab1:
    st.header("Gemini AI")
    input_text = st.text_input("Type something:", key="text_input")
    
    if st.button("Generate", key="text_response"):
        if input_text:
            response = get_gemini_response(input_text)
            st.subheader("Response:")
            st.write(response)
        else:
            st.warning("Please enter some text!")

#Tab 2: Text and Image
with tab2:
    st.header("Gemini AI")
    input_text = st.text_input("Type something:", key="text_and_image_input")
    uploaded_file = st.file_uploader("upload an image...", type=["jpg", "jpeg", "png"])
    
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    if st.button("Generate", key="image_text_response"):
        if input_text or image:
            response = get_gemini_response(input_text, image)
            st.subheader("Response:")
            st.write(response)
        else:
            st.warning("Please provide either text, an image, or both!")