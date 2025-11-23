# Positional Encodings

## Why Needed
Transformers process all tokens in parallel, losing sequence order information. Positional encodings add position information to embeddings.

## How It Works
- Add positional vectors to token embeddings before feeding to transformer
- Uses sine/cosine functions at different frequencies:
  - `PE(pos, 2i) = sin(pos / 10000^(2i/d))`
  - `PE(pos, 2i+1) = cos(pos / 10000^(2i/d))`
- Where `pos` = position, `i` = dimension, `d` = embedding dimension

## Key Properties
- Deterministic (same position always gets same encoding)
- Unique encoding for each position
- Model can learn to attend to relative positions
- Works for sequences longer than training data

## Alternative: Learned Positional Embeddings
- Train position embeddings like word embeddings
- Used in BERT, GPT
- Fixed maximum sequence length

## Eg 

text - Uzair eats biryani

tokinized - 200264, 17360, 200266, 3575, 553, 261, 10297, 29186, 200265, 200264, 1428, 200266, 90573, 1517, 88971, 3742, 88, 3048, 200265, 200264, 173781, 200266

text - biryani eats Uzair

tokinized - 200264, 17360, 200266, 3575, 553, 261, 10297, 29186, 200265, 200264, 1428, 200266, 65, 23965, 3048, 88971, 61829, 1517, 200265, 200264, 173781, 

here the positional encoding will help the model understand that "Uzair" is the subject in the first sentence and the object in the second, despite having the same tokens.

***IMP***
The model knows the words,
but doesn’t know which word came first, second, third, etc.

So we need a system that tells the model:

the order of the words

where each word is located in the sentence

This system is called Positional Encoding.


**📦 What it actually does**

Every word is converted into a vector (embedding).
Positional encoding adds extra numbers that represent position:

Example (simple):

Word	Word Vector	Position Vector	Final Input
Uzair	[0.5, 1.2, …]	[0.1, 0.98, …]	Sum of both
eats	[1.4, 0.7, …]	[0.2, 0.74, …]	Sum
biryani	[0.9, 0.1, …]	[0.3, 0.51, …]	Sum

Now the model knows:

“Uzair” comes before “eats”

“eats” comes before “biryani”

**📌 Why not just use 1, 2, 3 as positions?**

Because:

Text can be thousands of tokens long

The model needs something continuous and smooth

It must allow the model to understand relationships like:

word at position 2 is close to position 3
word at position 2000 is far away

The chosen method makes it easy for the model to learn:

“closeness”

“distance”

“pattern of order”