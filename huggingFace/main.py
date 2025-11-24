from transformers import pipeline
pipe = pipeline("image-text-to-text", model="google/gemma-3n-E4B-it")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    },
]
pipe(text=messages)

'''
what it does is:
it download the model on your local machine and run inference there... so no api calls are made... 
ur just need to have enough disk space and ram to load the model.
ur just running the model locally.
it uses the gemma-3n-E4B-it model from huggingface to answer questions about images.

usage:
use huggingface transformers library to run the model locally.
'''