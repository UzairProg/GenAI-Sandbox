# persona based prompting
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = ''''
You are a AI persona assistant named Uzair.
you are acting on behalf of Uzair a 19 year old programming enthusiast from India.
you love coding, technology, and exploring new advancements in AI.
your main tech stack includes Python, JavaScript, and web development frameworks like React and Node.js. MERN stack is your forte.

Examples:
User: Hi there! Can you tell me about yourself?
Assistant: Hi Buddy! I'm Uzair, a 19-year-old programming enthusiast from India. How can I assist you today?
'''

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you help me with a coding problem?"}
    ]
)

print(response.choices[0].message.content)

'''
here, we have defined a persona for the Gemini model to act as "Uzair", a 19-year-old programming enthusiast from India.
this persona-based prompting helps in tailoring the model's responses to align with the characteristics, interests, and expertise of the defined persona.
by providing specific details about Uzair's background, interests, and tech stack, we guide the model to respond in a manner consistent with this persona.
this technique is useful for creating more engaging and contextually relevant interactions, especially in applications like chatbots, virtual assistants, or any scenario where a consistent character or role is desired.

****************IMPORTANT****************
persona-based prompting allows us to define a specific character or role for the AI model to embody during interactions.
this helps in generating responses that are more aligned with the desired personality, expertise, and context.
it enhances user engagement by providing a consistent and relatable experience.
'''
