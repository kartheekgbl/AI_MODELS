import streamlit as st
import requests

# Set page config
st.set_page_config(page_title="RamaSethu Chatbot", layout="centered")

# Model options
model_options = ['mistral', 'gemma:2b', 'llama3']
selected_model = st.selectbox("Choose a model", model_options)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("💬 Chat with Ollama")

# Chat message display
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Input for user message
if prompt := st.chat_input("Type your message..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Call to Ollama local server
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": selected_model,
                "prompt": prompt,
                "stream": False
            }
        )
        if response.status_code == 200:
            bot_reply = response.json()["response"]
        else:
            bot_reply = f"⚠️ Error: {response.status_code} - {response.text}"
    except Exception as e:
        bot_reply = f"🚫 Connection error: {e}"

    # Add bot reply to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

    # Rerun the app to update chat
    st.rerun()
