import os
import base64
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Download and encode image
image_url = "https://images.pexels.com/photos/34298347/pexels-photo-34298347.jpeg"
image_data = requests.get(image_url).content
base64_image = base64.b64encode(image_data).decode('utf-8')

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content":[
            {"type": "text", "text": "describe this image in 50 words"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]},
    ]
)

print(response.choices[0].message.content)
