import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing!")

client = genai.Client()

print("Gemini is thinking...\n")

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how large language models work in simple terms.",
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)