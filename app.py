import streamlit as st
import google.generativeai as genai  # Placeholder for Google Generative AI library
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables (optional, for non-API key related data)
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Smart ATS",
    page_icon="‍",
    layout="centered",
)

# Sidebar to input placeholder for Google API Key
st.sidebar.title("Smart ATS Configuration")
API_KEY_PLACEHOLDER = "AIzaSyD2oLQHkz9sYQvKZN6VaZ7ZI2t2N79wefQ"  # Placeholder for actual API key
st.sidebar.text_input("Enter your Google API Key", type="password", value=API_KEY_PLACEHOLDER)
st.sidebar.subheader("Don't have a Google API Key?")
st.sidebar.write("Visit [Google Makersuite](https://makersuite.google.com/app/apikey) and log in with your Google account. Then click on 'Create API Key'.")

# Important note: Replace `API_KEY_PLACEHOLDER` with your actual Google API key before running the code.

# Function to configure Gemini AI model (assuming API key is set elsewhere)
def configure_gemini_api():
    # Replace with actual configuration logic using the provided API key
    pass

# Comment out or remove the following line if `configure_gemini_api` is implemented
# configure_gemini_api(API_KEY_PLACEHOLDER)  # Placeholder configuration (assuming API key is set elsewhere)

# Function to get response from Gemini AI (assuming API key is available)
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')  # Assuming Gemini Pro model is used
    response = model.generate_content(input)
    return response.text

# Function to extract text from uploaded PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analyst
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide the 
best assistance for improving the resumes. Assign the percentage Matching based 
on JD and the missing keywords with high accuracy.
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

## Streamlit app
st.title("Resume Matcher ATS")

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)

        # Placeholder for handling API key and potential errors
        try:
            # Replace with actual logic to use the API key and call get_gemini_response
            response = get_gemini_response(input_prompt.format(text=text, jd=jd))
            st.subheader("Response:")
            parsed_response = json.loads(response)
            for key, value in parsed_response.items():
                st.write(f"**{key}:** {value}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.warning("Make sure you have a valid Google API key and the Generative AI library is configured correctly.")














'''import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Smart ATS",
    page_icon="👨‍💼",
    layout="centered",
)

# Sidebar to input Google API Key
st.sidebar.title("Smart ATS Configuration")
API_KEY = st.sidebar.text_input("Enter your Google API Key", type="password")
st.sidebar.subheader("Don't have a Google API Key?")
st.sidebar.write("Visit [Google Makersuite](https://makersuite.google.com/app/apikey) and log in with your Google account. Then click on 'Create API Key'.")

# Check if API key is provided
if not API_KEY:
    st.error("Please enter your Google API Key.")
    st.stop()

# Function to configure Gemini AI model with the provided API key
def configure_gemini_api(api_key):
    genai.configure(api_key=api_key)

# Configure Gemini AI model with the provided API key
configure_gemini_api(API_KEY)

# Function to get response from Gemini AI
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from uploaded PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analyst
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide the 
best assistance for improving the resumes. Assign the percentage Matching based 
on JD and the missing keywords with high accuracy.
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

## Streamlit app
st.title("Resume Matcher ATS")

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))
        st.subheader("Response:")
        parsed_response = json.loads(response)
        for key, value in parsed_response.items():
            st.write(f"**{key}:** {value}")
'''
