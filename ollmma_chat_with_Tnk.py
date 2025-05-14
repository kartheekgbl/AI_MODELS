import tkinter as tk
from tkinter import scrolledtext
import requests

# Function to get the bot's response from Ollama
def chat_with_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",  # Using Mistral model
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Function to handle sending the user's message
def send_message():
    user_input = entry.get()
    if user_input.lower() in ["exit", "quit"]:
        window.quit()

    # Display user message
    chat_box.config(state=tk.NORMAL)  # Enable editing of chat box
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    chat_box.yview(tk.END)  # Scroll to the bottom
    chat_box.config(state=tk.DISABLED)  # Disable editing of chat box

    # Get bot response
    bot_response = chat_with_ollama(user_input)

    # Display bot response
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_box.yview(tk.END)
    chat_box.config(state=tk.DISABLED)  # Disable editing of chat box

    # Clear entry field
    entry.delete(0, tk.END)

# Set up the main window
window = tk.Tk()
window.title("Chat with Mistral Bot")

# Create a scrollable chat box
chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_box.grid(row=0, column=0, padx=10, pady=10)

# Entry field for user input
entry = tk.Entry(window, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

# Send button to send the message
send_button = tk.Button(window, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
