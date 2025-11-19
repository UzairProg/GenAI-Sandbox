Tokens are the basic units language models use to read and write text — short chunks that can be whole words, subwords, or characters depending on the tokenizer.
Models turn text into tokens, process sequences of tokens, then decode tokens back to text.
Token counts determine a model's context window, affect cost and truncation, and are the unit used for billing and limits.
In short: tokens = how an LLM segments, reasons about, and measures text.

eg for gpt-3.5-turbo:

Hi i am uzair 

is converted into 5 tokens:

["Hi", " i", " am", " uz", "air"]

<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hi i am uzair<|im_end|>
<|im_start|>assistant
["Hi", " i", " am", " uz", "air"] (5 tokens)<|im_end|>

[100264, 9125, 198, 2675, 527, 264, 11190, 18328, 100265, 198, 100264, 882, 198, 13347, 602, 1097, 45576, 1334, 100265, 198, 100264, 78191, 198]

now this [100264, 9125, 198, 2675, 527, 264, 11190, 18328, 100265, 198, 100264, 882, 198, 13347, 602, 1097, 45576, 1334, 100265, 198, 100264, 78191, 198] is the token ids representation of the same text.

***Important:***
this ids what the model actually processes. this ids will be passed to the transformer model. and this model will predict the next token id based on the previous token ids.

[........, 100264, 78191, 198] -> model -> [........, 100264, 78191, 198, ***89023***]

For more details on how tokens work and why they matter, see the [Tokenization](./tokenization.md) page.