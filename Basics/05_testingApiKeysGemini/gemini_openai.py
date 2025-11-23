from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": "Hello, world!"}
    ]
)

print(response.choices[0].message.content)

'''
here, we are using the OpenAI Python client to interact with Google's Gemini model.
We set the `api_key` and `base_url` parameters to point to the Gemini API endpoint.
We then create a chat completion using the Gemini model "gemini-2.5-flash" and print the response.

in simple words, this code allows us to use the OpenAI client library to access and utilize Google's Gemini language model for generating chat completions.
'''