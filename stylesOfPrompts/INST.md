# INST Prompting (Instruction Style Prompting)

used in models like Anthropic's Claude and Meta's LLaMA series.

# INST Prompting Style

### <INST> Instruction: <USER_PROMPT> </INST>

It’s a prompt format that clearly delineates instructions using special tags.
The idea:
➡️ Wrap instructions in `<INST>` and `</INST>` tags
➡️ Clearly separate the instruction from the user prompt
➡️ Helps models understand the task better
Used in models like Anthropic's Claude and Meta's LLaMA series.

# Example
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "<INST> Instruction: Write a Python program to print 'Hello, World!' </INST>"}
    ]
)
in INST style prompt would look like:
### <message start> <INST> Instruction: Write a Python program to print 'Hello, World!' </INST> <message end>