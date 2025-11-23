# Structured Outputs with few Short prompting
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key = API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = '''You are an expert in coding and respond questions related to coding only.
If the user asks something other than coding, reply with, I can only help you with coding questions.

rules:
- Always respond in JSON format.
- the JSON oject should have two keys: "code" and "isCodingQuestion".
- {{
    "code": <the code snippet or an null if not a coding question>,
    "isCodingQuestion": <true or false>
}}

Example 1:
User: Solve the equation 2x + 3 = 7 for x.
Assistant:
{{
    "code": null,
    "isCodingQuestion": false
}}

Example 2:
User: write a python program to Solve the equation 2x + 3 = 7 for x.
Assistant:
{{
    "code": "```python\ndef solve_equation():\n    # Solving 2x + 3 = 7\n    x = (7 - 3) / 2\n    return x\nprint(\"The value of x is:\", solve_equation())\n```",
    "isCodingQuestion": true
}}
'''
prompt = "write a python program to Solve the equation 2x + 3 = 7 for x."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)

'''
here, we are using few-shot prompting to guide the Gemini model's behavior towards providing structured outputs in JSON format.

we're telling the model to respond in a specific JSON structure with two keys: "code" and "isCodingQuestion".
with examples provided in the system prompt, the model learns how to format its responses accordingly.

this is particularly useful when we want to ensure that the model's outputs can be easily parsed and utilized in downstream applications, such as automated code generation or analysis tools.

this is called sturctured outputs with few-shot prompting, where we set rules and provide examples to achieve the desired output format.

'''