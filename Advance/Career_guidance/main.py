import streamlit as st
import base64
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OpenAI API key not found! Please set it in your environment variables.")
    st.stop()

st.set_page_config(page_title="Career Guidance", page_icon="", layout="centered")
st.title("Career Guidance")
waht_help = st.text_input("Upload your resume and let the AI critique it!")
ask = st.button("Ask")


    
