from dotenv import load_dotenv
from groq import Groq
load_dotenv()
import os
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
print("GROQ_API_KEY:", os.environ["GROQ_API_KEY"])

promt=input("Me:")


client = Groq()
completion = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[
    {
        "role": "assistant",
        "content": promt
    },
    {
        "role": "assistant",
        "content": "<think>\nOkay, the user sent an empty message. Maybe they're testing or just trying to see if I'm responsive. I should acknowledge their message and ask if they need help with something. Keep it friendly and open-ended.\n\nFirst, I'll say \"Hello!\" to start the conversation. Then, offer assistance by asking if there's anything they need help with. That should encourage them to respond with their actual request. Make sure the tone is welcoming and not too formal. Keep it simple and approachable.\n</think>\n\nHello! How can I assist you today? 😊"
    },
    {
        "role": "user",
        "content": ""
    }
    ],
    temperature=0.6,
    max_completion_tokens=4096,
    top_p=0.95,
    reasoning_effort="default",
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[-1].delta.content or "", end="")

