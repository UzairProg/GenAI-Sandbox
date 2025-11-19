import tiktoken

en = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! my name is Uzair"
tokens = en.encode(text)

print(f"Text: {text}")
print(f"Tokens: {tokens}") # [25216, 1354, 0, 922, 1308, 382, 61829, 1517]

decoded_text = en.decode([25216, 1354, 0, 922, 1308, 382, 61829, 1517]) # passing the same token list
print(f"Decoded Text: {decoded_text}") # "Hey there! my name is Uzair"