# RAG (Retrieval Augmented Generation)

## What is RAG?
RAG combines retrieval systems with LLMs to provide accurate, context-aware responses using external knowledge.

**Problem it solves**: LLMs have knowledge cutoffs and can hallucinate. RAG grounds responses in real data.

## How RAG Works
1. **Index**: Convert documents → embeddings → store in vector DB
2. **Retrieve**: User query → embedding → find similar vectors
3. **Augment**: Inject retrieved context into LLM prompt
4. **Generate**: LLM produces answer based on retrieved facts

```
User Query → Embed → Vector Search → Top-K Docs → LLM + Context → Answer
```

## Key Components
- **Embeddings**: Text → dense vectors (e.g., OpenAI `text-embedding-3-small`)
- **Vector DB**: Stores & searches embeddings efficiently (Qdrant, Pinecone, Weaviate)
- **Chunking**: Split docs into manageable pieces (512-1024 tokens)
- **Retrieval**: Cosine similarity / ANN search for relevant chunks
- **Prompt**: `"Context: {retrieved_docs}\n\nQuestion: {query}\nAnswer:"`

---

# Qdrant Vector Database

## What is Qdrant?
Open-source vector database optimized for similarity search and RAG applications.

## Core Concepts

### Collections
- Container for vectors with same dimensionality
- Think: table in SQL, index in Elasticsearch
- Example: `documents_collection` for 1536-dim OpenAI embeddings

### Vectors
- Dense numerical representations (e.g., `[0.23, -0.45, 0.12, ...]`)
- Each vector has an ID and optional payload (metadata)

### Payload
- Metadata attached to each vector
- JSON format: `{"text": "...", "source": "...", "page": 3}`
- Filterable during search

### Distance Metrics
- **Cosine**: Measures angle (best for normalized embeddings)
- **Euclidean**: L2 distance
- **Dot Product**: Raw similarity score

## Qdrant Workflow

### 1. Setup
```python
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(":memory:")  # or url="http://localhost:6333"

# Create collection
client.create_collection(
    collection_name="docs",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)
```

### 2. Insert (Upsert)
```python
from openai import OpenAI
openai_client = OpenAI()

# Generate embedding
text = "RAG improves LLM accuracy"
embedding = openai_client.embeddings.create(
    model="text-embedding-3-small",
    input=text
).data[0].embedding

# Insert into Qdrant
client.upsert(
    collection_name="docs",
    points=[{
        "id": 1,
        "vector": embedding,
        "payload": {"text": text, "source": "notes.md"}
    }]
)
```

### 3. Search
```python
# Query embedding
query = "How does RAG work?"
query_vec = openai_client.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

# Search similar vectors
results = client.search(
    collection_name="docs",
    query_vector=query_vec,
    limit=3
)

for hit in results:
    print(f"Score: {hit.score}, Text: {hit.payload['text']}")
```

### 4. Filter Search
```python
from qdrant_client.models import Filter, FieldCondition, MatchValue

results = client.search(
    collection_name="docs",
    query_vector=query_vec,
    query_filter=Filter(
        must=[FieldCondition(key="source", match=MatchValue(value="notes.md"))]
    ),
    limit=5
)
```

## RAG + Qdrant Pipeline

```python
# 1. Chunk & embed documents
chunks = chunk_document(doc)
for i, chunk in enumerate(chunks):
    vec = get_embedding(chunk)
    client.upsert("docs", points=[{
        "id": i,
        "vector": vec,
        "payload": {"text": chunk}
    }])

# 2. Query time
query = "What is tokenization?"
query_vec = get_embedding(query)

# 3. Retrieve top-k
results = client.search("docs", query_vector=query_vec, limit=3)
context = "\n".join([r.payload["text"] for r in results])

# 4. Generate answer
prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
response = llm.complete(prompt)
```

## Qdrant Features
- **Filtering**: Combine vector search with metadata filters
- **Payloads**: Store rich metadata (text, timestamps, tags)
- **Quantization**: Reduce memory (scalar/product quantization)
- **Sharding**: Horizontal scaling across nodes
- **HNSW Index**: Fast approximate nearest neighbor search
- **Snapshots**: Backup & restore collections

## Common Use Cases
- **Document Q&A**: Search internal docs, wikis, PDFs
- **Semantic Search**: Find similar products, articles, code
- **Recommendation**: Similar items based on embeddings
- **Chatbots**: Context-aware responses from knowledge base

## Qdrant vs Alternatives
| Feature | Qdrant | Pinecone | Weaviate |
|---------|--------|----------|----------|
| Open Source | ✅ | ❌ | ✅ |
| Self-hosted | ✅ | ❌ | ✅ |
| Filtering | ✅ | ✅ | ✅ |
| Free Tier | ✅ (self-host) | ✅ (cloud) | ✅ (cloud) |

## Quick Start
```bash
# Install
pip install qdrant-client openai

# Run Qdrant locally (Docker)
docker run -p 6333:6333 qdrant/qdrant

# Or use in-memory mode (no Docker)
client = QdrantClient(":memory:")
```

## Key Takeaways
- RAG = Retrieval + LLM for grounded answers
- Qdrant = Vector DB for fast similarity search
- Embeddings bridge text and vector space
- Pipeline: Chunk → Embed → Store → Search → Generate
- Filters + metadata enable precise retrieval
