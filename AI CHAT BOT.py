import streamlit as st
from google import genai

# Get API key from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 Gemini AI Chatbot")
st.write("Ask Gemini anything!")

# User prompt
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words..."
)

# Generate response
if st.button("Generate Response"):

    if prompt.strip():

        with st.spinner("Gemini is thinking..."):

            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                st.success("Response generated!")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a prompt.")