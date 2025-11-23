from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from a .env file, without it the API key won't be found
API_KEY = os.getenv("GEMINI_API_KEY") # Get the Gemini API key from environment variables

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a maths expert. and answer only maths questions. and if the question is not related to maths, reply with, I can only help you with maths questions."},
        {"role": "user", "content": "write me a python program to print hello world!"}
    ]
)

print(response.choices[0].message.content)

'''
here, we have set up a system prompt that instructs the Gemini model to act as a maths expert.
this way, when the user asks a non-maths question, the model will respond accordingly, adhering to the defined role.

so we're restricting the model's responses to only maths-related queries by using a system prompt.

this is called prompt engineering, where we guide the model's behavior through carefully crafted instructions. 

****************IMPORTANT****************
system prompts are like special instructions that tell the AI how to respond in a conversation.
'''