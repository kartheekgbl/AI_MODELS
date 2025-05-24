import streamlit as st
from openai import OpenAI

# Set your OpenRouter API key
MODEL_API_KEY = "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"

# Initialize OpenAI client with OpenRouter base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=MODEL_API_KEY,
)

# Streamlit page config
st.set_page_config(page_title="GPT Chatbot", layout="centered")
st.title("🤖 GPT Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display past chat messages
for msg in st.session_state.messages[1:]:  # skip the system message
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call the OpenRouter model (deepseek)
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=st.session_state.messages
    )

    # Extract response
    reply = response.choices[0].message.content

    # Display assistant reply
    with st.chat_message("assistant"):
        st.markdown(reply)

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
