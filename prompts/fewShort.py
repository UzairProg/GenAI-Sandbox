# few Short prompting - This prompt provides a few examples to the model to perform a task.
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = '''You are a coding expert. reply only question related to coding, 
if user asks something other than coding, reply with, I can only help you with coding questions.

Example 1:
User: Solve the equation 2x + 3 = 7 for x.
Assistant: Sorry, I can only help you with coding questions.

Example 2:
User: write a python program to Solve the equation 2x + 3 = 7 for x.
Assistant: 
```python
def solve_equation():
    # Solving 2x + 3 = 7
    x = (7 - 3) / 2
    return x
print("The value of x is:", solve_equation())
```

'''

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
'''
here, we are using few-shot prompting to guide the Gemini model's behavior.
in this method, we provide the model with examples of how to respond to certain types of questions with prompts too.

and in real use cases, few-shot prompting can significantly improve the model's performance on specific tasks by giving it context and examples to follow.
even by 50-70% in some scenarios.
this technique is particularly useful when we want the model to adhere to specific guidelines or formats in its responses.
'''