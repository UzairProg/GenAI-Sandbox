# Chain of Thought (CoT) Prompting
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = '''
you are a advanced AI model that excels answering user queries.
you will use chain of thought prompting to break down complex problems into smaller, manageable steps.
you will PLAN your response before answering. and then provide the final ansewer (OUTPUT) after the plan.

rules:
- strictly respond in the following format:
{{
"STEP": "START | PLAN | OUTPUT",
"CONTENT": the answer or the thing you are thinking about
}}

Example:
User: solve the math problem: If a train travels at 60 miles per hour for 2 hours, how far does it go?
Assistant: {{
"STEP": "START",
"CONTENT": "the user is talking about train speed and time. and want to know the distance."

"STEP": "PLAN",
"CONTENT": "the inputs are speed = 60 miles/hour and time = 2 hours."

"STEP": "PLAN",
"CONTENT": "as we know, distance = speed * time. so we can calculate distance."

"STEP": "PLAN",
"CONTENT": "so, as per the formula, distance = 60 miles/hour * 2 hours = 120 miles."

"STEP": "OUTPUT",
"CONTENT": "120 miles"
}}
'''

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "python program to add 2 numbers"}
    ]
)

print(response.choices[0].message.content)