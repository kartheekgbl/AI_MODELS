import requests

def chat_with_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False  # Set to True for real-time streaming
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    reply = chat_with_ollama(user_input)
    print("Bot:", reply)
