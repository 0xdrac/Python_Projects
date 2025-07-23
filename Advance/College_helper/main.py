import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OpenAI API key not found! Please set it in your environment variables.")
    st.stop()

st.set_page_config(page_title="📚College Helper", page_icon="", layout="centered")
st.title("College Helper (AKA SHIRO)")
st.subheader("If you need any help with college you can ask me, i will help you in any means possible :")

ask = st.text_input("What help you need my child?")
ask_button = st.button("Ask SHIRO")

if ask and ask_button:
    if ask.strip():
        try:
            client = OpenAI(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI career counselor."},
                    {"role": "user", "content": ask}
                ]
            )
            st.markdown("### AI Response:")
            st.write(response['choices'][0]['message']['content'])
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")

    
