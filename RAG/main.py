from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

pdf_path = Path(__file__).parent / "nodeJsNotes.pdf" # here, Path(__file__) gives the current file path i.e. RAG/main.py.. so its parent is RAG/ .. and then we append nodeJsNotes.pdf to it.

#load the pdf in the python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# print(docs[0])

#split doc into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400, # also includes overlapping part of prev chunk.. so to get a little content of the prev chunk too
)

chunks = text_splitter.split_documents(documents=docs)

print(f"Total Chunks: {len(chunks)}")
print(chunks[0])  #print first chunk

# vector embeddings - using free local HuggingFace model (no API quota limits)
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
print("Using local HuggingFace embeddings - no API calls needed!")

# connect to Qdrant vector db
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="learning-rag",
    url="http://localhost:6333"  # assuming Qdrant is running locally on default port
)

print("indexing completed.")

'''
rn this code is sync in nature. it blocks further execution until indexing is done.
and that's not how its done in production systems.

in production systems, we use async processing and task queues.
so we need to make it async and push the indexing tasks to a task queue like Celery or RQ.

async - lets do this in background, dont block the main thread, and let user do what they want to do.
'''