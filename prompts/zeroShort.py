#Zero Short Prompting - This prompt is to directly ask the model to perform a task without any examples.
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = "You are a coding expert. reply only question related to coding, if user asks something other than coding, reply with, I can only help you with coding questions."

prompt_1 = "Solve the equation 2x + 3 = 7 for x."
prompt_2 = "write a python program to Solve the equation 2x + 3 = 7 for x."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt_2}
    ]
)

print(response.choices[0].message.content)