import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


# vector embeddings - using free local HuggingFace model (no API quota limits)
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="learning-rag",
    url="http://localhost:6333" # assuming Qdrant is running locally on default port
)

user_query = input("Search something: ")

# perform similarity search - returns relevent chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join(f"Page Content: {result.page_content}]\n Page Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
 for result in search_results)

SYSTEM_PROMPT = f'''
you are a helpful AI assistant. who answers user queries based on the provided context.
context is retrieved from a pdf document along with page number and file location.
use the context to answer the user query.
give the answer nicely formatted with bullet points if required. use the context nicely and answer in the best way possible.
context:{context}
rules:
- answer based on the provided context.
- if the context does not contain the answer, reply "I don't know".
'''

# user_prompt = input("👉")
message_history = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=message_history
)

raw_response = response.choices[0].message.content
print("💡", raw_response)