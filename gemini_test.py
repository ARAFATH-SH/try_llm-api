import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing!")

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain machine learning."
)

print(response.output_text)
