# Prompt Styles - it means the way we prompt the model to get desired outputs. there are various styles of prompting that can be used based on the use case.

till now we have implemented the following styles of prompting:
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt_2}
    ]
)

# Alpaca Style Prompting

### Instructions: <SYSTEM_PROMPT>\n
### Input: <USER_PROMPT>\n
### Response: \n

It’s a prompt format introduced by Stanford’s Alpaca model, inspired by LLaMA.
The idea:
➡️ Give the model a clear instruction
➡️ Optionally give input/context
➡️ Then ask it to produce an output

Very clean. Very structured.
Used heavily for fine-tuning LLMs.

# Example

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a maths expert. and answer only maths questions. and if the question is not related to maths, reply with, I can only help you with maths questions."},
        {"role": "user", "content": "write me a python program to print hello world!"}
    ]
)

in alpaca style prompt would look like:

### Instruction:
You are a maths expert. Only answer maths questions.
If the question is not related to maths, reply with:
"I can only help you with maths questions."

### Input:
write me a python program to print hello world!

### Response: \n
