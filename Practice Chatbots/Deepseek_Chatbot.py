import streamlit as st
from openai import OpenAI

# Set up OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"],  # Use Streamlit Secrets
)

# App title
st.title("🧠 Karnagpt Chatbot (OpenRouter)")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Say something...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate reply
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                completion = client.chat.completions.create(
                    model="deepseek/deepseek-r1:free",
                    messages=st.session_state.messages,
                    extra_headers={
                        "HTTP-Referer": "https://karnagpt.streamlit.app",  # Optional
                        "X-Title": "KarnaGPT",                             # Optional
                    },
                )
                reply = completion.choices[0].message.content
            except Exception as e:
                reply = f"⚠️ Error: {e}"

            st.markdown(reply)

    # Add assistant reply to history
    st.session_state.messages.append({"role": "assistant", "content": reply})
