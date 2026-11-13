import os
from google import genai
from google.genai import errors

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing!")

client = genai.Client()

try: 
    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain machine learning."
    )
    print(response.output_text)

except errors.APIError as e:
    print("Gemini API error", e.code)
    print(e.message)
