import streamlit as st
import requests
import pyttsx3
import speech_recognition as sr
from io import BytesIO
from PIL import Image
import openai  # For DALL·E image generation

# Set page config
st.set_page_config(page_title="RamaSethu Chatbot", layout="centered")

# Model options
model_options = ['mistral', 'gemma:2b', 'llama3']
selected_model = st.selectbox("Choose a model", model_options)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("💬 Chat with Karna")

# Chat message display
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Function to convert text to speech (voice output)
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech (voice input)
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I could not understand. Please try again."
        except sr.RequestError:
            return "Sorry, I'm having trouble with the speech recognition service."

# Function to generate images from text (using DALL·E API)
def generate_image_from_text(prompt):
    openai.api_key = "your-openai-api-key"
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    image_response = requests.get(image_url)
    return Image.open(BytesIO(image_response.content))

# Add buttons for voice input and image generation
col1, col2 = st.columns([1, 3])

with col1:
    if st.button("🎤 Use Voice Input"):
        user_input = speech_to_text()
        st.session_state.chat_history.append({"role": "user", "content": user_input})

with col2:
    if st.button("🖼️ Generate Image from Prompt"):
        prompt = st.text_input("Enter prompt to generate image:")
        if prompt:
            image = generate_image_from_text(prompt)
            st.image(image, caption="Generated Image")

# Input for user message
user_prompt = st.chat_input("Type your message...")
if user_prompt:
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Call to Ollama local server
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": selected_model,
                "prompt": user_prompt,
                "stream": False
            }
        )
        if response.status_code == 200:
            bot_reply = response.json()["response"]
        else:
            bot_reply = f"⚠️ Error: {response.status_code} - {response.text}"
    except Exception as e:
        bot_reply = f"🚫 Connection error: {e}"

    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
    text_to_speech(bot_reply)

