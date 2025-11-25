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
        {"role": "user", "content": "how's the weather in Goa today rn in degrees realtime"}
    ]
)

print(response.choices[0].message.content)

'''
The llm cant provide the realtime weather data, as llm is trained on a specific dataset.. and it have info or general info of that data only
so it cant give the realtime data to me

eg:
Here's the current weather in Goa (as of my last update, **approximately 11:30 PM IST on June 10, 2024**):
this is the response llm gave.. 2024's data its the last data he remebered/trained on and based on it he's telling be the info
'''