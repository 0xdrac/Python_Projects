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

st.set_page_config(page_title="Image Location Recognizer", page_icon="🖼️", layout="centered")
st.title("🖼️ Image Location Recognizer")
st.markdown("Upload an image and the AI will provide a rough idea of where the picture was taken.")

uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
analyze = st.button("Analyze Image")

def encode_image_to_base64(image_bytes):
    return base64.b64encode(image_bytes).decode("utf-8")

if analyze:
    if not uploaded_image:
        st.warning("Please upload an image file.")
        st.stop()
    try:
        # Read and encode the image
        image_bytes = uploaded_image.read()
        image_b64 = encode_image_to_base64(image_bytes)

        # Initialize OpenAI client
        client = OpenAI(api_key=OPENAI_API_KEY)

        # Compose messages for chat completion
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert travel guide. Given an image, "
                    "you provide a rough idea of the location where it could have been taken. "
                    "If uncertain, give your best guesses based on visible features."
                )
            },
            {
                "role": "user",
                "content": "Please analyze this image and guess the location.",
                "image": {"base64": image_b64}
            }
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        st.markdown("### Location Analysis")
        st.markdown(response.choices[0].message.content.strip())
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
