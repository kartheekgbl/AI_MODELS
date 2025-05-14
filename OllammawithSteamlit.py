import streamlit as st
import requests

# Function to interact with Ollama (or OpenAI) API
def chat_with_ollama(prompt):
    url = "http://localhost:11434/api/generate"  # For Ollama
    payload = {
        "model": "mistral",  # Use the model you want (like Mistral, Gemma, etc.)
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Set up the Streamlit page
st.title("Chat with Mistral Bot")

# Create a text area for user input
user_input = st.text_input("You: ", "")

# If user has entered a message, send it to the bot
if user_input:
    # Get response from the bot (Ollama or OpenAI)
    bot_response = chat_with_ollama(user_input)
    
    # Display the conversation in the Streamlit app
    st.write(f"You: {user_input}")
    st.write(f"Bot: {bot_response}")

