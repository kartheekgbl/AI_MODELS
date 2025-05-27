import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
MODEL_API_KEY = os.getenv("API_KEY")

# Validate the API key before proceeding
if not MODEL_API_KEY:
    st.error("API Key not found. Please set API_KEY in your .env file.")
    st.stop()

# Initialize OpenAI client with OpenRouter base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=MODEL_API_KEY,
)

# Streamlit page configuration
st.set_page_config(page_title="GPT Chatbot", layout="centered")
st.title("🤖 Karna GPT")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display past chat messages
for msg in st.session_state.messages[1:]:  # Skip system message
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call the model
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content

        # Display assistant reply
        with st.chat_message("assistant"):
            st.markdown(reply)

        # Save assistant reply to chat history
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"An error occurred: {e}")
