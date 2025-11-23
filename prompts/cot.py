# Chain of Thought (CoT) Prompting
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

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
if there's a code snippet involved, structure it properly, readable format.
rules:
- strictly respond in the following format:
- and reply in proper structured json format.
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
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "python program to add 2 numbers"},

        #putting the data manually as per the responses we're getting from the model.
        {"role": "assistant", "content": json.dumps({
            "STEP": "START",
            "CONTENT": "The user wants a Python program that takes two numbers and adds them. I need to write the Python code for this."
        })},

        {"role": "assistant", "content": json.dumps({
"STEP": "PLAN",
"CONTENT": "I will define a function that takes two arguments. Inside the function, I will add the two arguments. I will then call this function with example numbers and print the result. I should also consider getting input from the user for the numbers."
})},

        {"role": "assistant", "content": json.dumps({
"STEP": "PLAN",
"CONTENT": [
"Define a function, e.g., `add_numbers`, that accepts two parameters.",
"Inside the function, calculate the sum of the two parameters.",
"Optionally, get input from the user for the two numbers. This will make the program interactive.",
"Convert the user input to integers or floats, as input() returns strings.",
"Call the `add_numbers` function with the user-provided numbers.",
"Print the result."
]
})},


    ]
)


print(response.choices[0].message.content)