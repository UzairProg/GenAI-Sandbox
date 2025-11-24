# ChatML Prompting Style

uptill now in prompt repo and examples, we have used this chatML style of prompting.
It's the format used by OpenAI's ChatGPT and other chat-based models.

# ChatML Prompting
{
    "role": "user | system | assistant",
    "content": string  # the conetet of the role selected
}

# Example
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt_2}
    ]
)
