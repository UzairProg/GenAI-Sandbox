# Chain of Thought (CoT) Prompting
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def get_weather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The Weather in {city} is {response.text}"

    else:
        return "Something went wrong!"
    
available_tools = {
    "get_weather": get_weather
}

SYSTEM_PROMPT = '''
you are a advanced AI model that excels answering user queries.
you will use chain of thought prompting to break down complex problems into smaller, manageable steps.
you will PLAN your response before answering. and then provide the final ansewer (OUTPUT) after the plan.
if there's a code snippet involved, structure it properly, readable format.
You can also call a tool if required from available list of tools
for every tool call wait for the observe step which is output for the called tool

rules:
- strictly respond in the following format:
- and reply in proper structured json format.

Available Tools:
- get_weather

{{
"STEP": "START | PLAN | OUTPUT",
"CONTENT": the answer or the thing you are thinking about
}}

Example 1:
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

Example 2:
User: How's the weather in delhi?
Assistant: {{
"STEP": "START",
"CONTENT": "The user wanna know the weather in delhi"

"STEP": "PLAN",
"CONTENT": "Let's see if we've a tool to get the weather info."

"STEP": "PLAN",
"CONTENT": "I need to use the get_weather tool with delhi as input."

"STEP": "TOOL",
"TOOL": "get_weather",
"INPUT": "delhi"

"STEP": "OBSERVE",
"TOOL": "get_weather",
"OUTPUT": "The Weather in delhi is Sunny +30°C"

"STEP": "PLAN",
"CONTENT": "Got the weather info from the tool."

"STEP": "OUTPUT",
"CONTENT": "The current weather in Delhi is Sunny with a temperature of 30 degrees Celsius."
}}
'''
user_prompt = input("👉")
message_history = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]
while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_response = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_response})

    parsed_results = json.loads(raw_response)

    if parsed_results.get("STEP") == "START":
        print("🔥", parsed_results.get("CONTENT"))
        continue
    if parsed_results.get("STEP") == "PLAN":
        print("🧠", parsed_results.get("CONTENT"))
        continue
    if parsed_results.get("STEP") == "TOOL":
        res = available_tools.get(parsed_results.get("TOOL"))(parsed_results.get("INPUT"))
        message_history.append({
            "role": "user",
            "content": f'''{{
            "STEP": "OBSERVE",
            "TOOL": "{parsed_results.get("TOOL")}",
            "OUTPUT": "{res}"
            }}'''
        })
        continue

    if parsed_results.get("STEP") == "OUTPUT":
        print("🤖", parsed_results.get("CONTENT"))
        break
