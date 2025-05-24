from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Function to get bot response from Ollama
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    bot_response = chat_with_ollama(user_input)
    return jsonify({"bot_response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
