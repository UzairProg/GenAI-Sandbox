from openai import OpenAI
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings

# Load .env from rag_queue directory
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# connect to Qdrant vector db
vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="learning-rag",
    url="http://localhost:6333"  # assuming Qdrant is running locally on default port
)

def process_query(query: str):
    print("Serching Chunks", query)
    search_results = vector_db.similarity_search(query=query)

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

    message_history = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query}
    ]

    response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=message_history
    )

    raw_response = response.choices[0].message.content
    print("💡", raw_response)
    return raw_response