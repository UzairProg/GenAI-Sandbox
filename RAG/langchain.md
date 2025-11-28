# LangChain

## What is LangChain?
Framework for building LLM-powered applications with modular components for chains, agents, memory, and retrieval.

**Core idea**: Chain together LLM calls, tools, and data sources to build complex workflows.

---

## Key Components

### 1. **LLMs & Chat Models**
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0.7)
response = llm.invoke("What is RAG?")
print(response.content)
```

### 2. **Prompts**
```python
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{question}")
])

chain = prompt | llm
response = chain.invoke({"question": "Explain embeddings"})
```

### 3. **Chains (LCEL)**
LangChain Expression Language - pipe operators for composing workflows.

```python
from langchain.schema.output_parser import StrOutputParser

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"question": "What is Qdrant?"})
```

### 4. **Document Loaders**
```python
from langchain_community.document_loaders import TextLoader, PyPDFLoader

# Load text file
loader = TextLoader("docs.txt")
documents = loader.load()

# Load PDF
pdf_loader = PyPDFLoader("manual.pdf")
pages = pdf_loader.load_and_split()
```

### 5. **Text Splitters**
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)
```

### 6. **Embeddings**
```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector = embeddings.embed_query("What is RAG?")
```

### 7. **Vector Stores**
```python
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

client = QdrantClient(":memory:")

vectorstore = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    client=client,
    collection_name="docs"
)
```

### 8. **Retrievers**
```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

relevant_docs = retriever.invoke("How does RAG work?")
```

### 9. **Memory**
```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)
memory.save_context({"input": "Hi"}, {"output": "Hello!"})
memory.load_memory_variables({})
```

---

## RAG with LangChain

### Simple RAG Chain
```python
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")
retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

result = qa_chain.invoke({"query": "What is tokenization?"})
print(result["result"])
print(result["source_documents"])
```

### Custom RAG Chain (LCEL)
```python
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

template = """Answer based on context:

Context: {context}

Question: {question}

Answer:"""

prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

answer = rag_chain.invoke("What is Qdrant?")
```

### Conversational RAG
```python
from langchain.chains import ConversationalRetrievalChain

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

conv_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

# First question
conv_chain.invoke({"question": "What is RAG?"})

# Follow-up (uses chat history)
conv_chain.invoke({"question": "How does it improve accuracy?"})
```

---

## Agents

Agents use LLMs to decide which tools to call and when.

### Create Tools
```python
from langchain.tools import Tool

def get_weather(city: str) -> str:
    return f"Weather in {city}: Sunny, 25°C"

weather_tool = Tool(
    name="get_weather",
    func=get_weather,
    description="Get current weather for a city"
)
```

### Agent with Tools
```python
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.tools import Tool

tools = [weather_tool]

agent = create_openai_functions_agent(
    llm=llm,
    tools=tools,
    prompt=ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ])
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
result = agent_executor.invoke({"input": "What's the weather in Tokyo?"})
```

### ReAct Agent (Reasoning + Acting)
```python
from langchain.agents import create_react_agent

react_agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt_template
)

agent_executor = AgentExecutor(
    agent=react_agent,
    tools=tools,
    verbose=True,
    max_iterations=5
)
```

---

## LangChain + Qdrant Full Example

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from qdrant_client import QdrantClient

# 1. Load documents
loader = TextLoader("knowledge.txt")
documents = loader.load()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# 3. Create embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 4. Store in Qdrant
client = QdrantClient(":memory:")
vectorstore = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    client=client,
    collection_name="knowledge"
)

# 5. Create retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 6. Build RAG chain
template = """Answer based on the context below. If you cannot answer, say "I don't know."

Context: {context}

Question: {question}

Answer:"""

prompt = ChatPromptTemplate.from_template(template)
llm = ChatOpenAI(model="gpt-4")

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 7. Ask questions
answer = rag_chain.invoke("What is tokenization?")
print(answer)
```

---

## Common Patterns

### Multi-Query Retrieval
Generate multiple query variations for better retrieval.
```python
from langchain.retrievers.multi_query import MultiQueryRetriever

multi_retriever = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm
)
```

### Compression Retrieval
Filter retrieved docs to only relevant parts.
```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)
```

### Self-Query Retrieval
Parse natural language queries into structured filters.
```python
from langchain.retrievers.self_query.base import SelfQueryRetriever

metadata_field_info = [
    {"name": "source", "description": "Document source", "type": "string"},
    {"name": "page", "description": "Page number", "type": "integer"}
]

sq_retriever = SelfQueryRetriever.from_llm(
    llm=llm,
    vectorstore=vectorstore,
    document_contents="Technical documentation",
    metadata_field_info=metadata_field_info
)
```

---

## Installation

```bash
# Core
pip install langchain langchain-openai langchain-community

# Qdrant integration
pip install langchain-qdrant qdrant-client

# Document loaders
pip install pypdf  # for PDF
pip install beautifulsoup4  # for web scraping
```

---

## Key Concepts Summary

| Component | Purpose |
|-----------|---------|
| **LLM** | Language model interface (OpenAI, Anthropic, etc.) |
| **Prompt** | Template for LLM input with variables |
| **Chain** | Combine components (LLM + prompt + parser) |
| **Document Loader** | Load data from files, URLs, databases |
| **Text Splitter** | Chunk documents for embeddings |
| **Embeddings** | Convert text to vectors |
| **Vector Store** | Store & search embeddings (Qdrant, Pinecone) |
| **Retriever** | Fetch relevant docs from vector store |
| **Memory** | Maintain conversation context |
| **Agent** | LLM decides which tools to call dynamically |

---

## LangChain vs Manual RAG

### LangChain
✅ Quick prototyping  
✅ Pre-built components  
✅ Easy switching (embeddings, LLMs, vector stores)  
❌ Abstraction overhead  
❌ Less control over details  

### Manual (Python + APIs)
✅ Full control  
✅ Optimized performance  
✅ Cleaner for production  
❌ More boilerplate  
❌ Reinvent integrations  

**Use LangChain for**: Prototyping, experimentation, multi-agent systems  
**Go manual for**: High-performance production, custom workflows

---

## Best Practices

1. **Chunk size**: 500-1000 tokens with 10-20% overlap
2. **Retrieval**: Start with k=3-5, tune based on precision/recall
3. **Prompts**: Be explicit about using context, handling unknowns
4. **Metadata**: Add source, timestamps for filtering & citations
5. **Evaluation**: Test retrieval quality before optimizing generation
6. **Memory**: Use for chat; avoid for one-off queries (adds latency)
7. **Agents**: Start simple (1-2 tools), add complexity gradually

---

## Resources

- [LangChain Docs](https://python.langchain.com/)
- [LangChain + Qdrant Guide](https://qdrant.tech/documentation/frameworks/langchain/)
- [LCEL Guide](https://python.langchain.com/docs/expression_language/)
- [RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
