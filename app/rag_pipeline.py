# rag_pipeline.py

from app.ingestion import load_documents_from_folder, chunk_documents
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

# Setup LLM and embeddings
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
embedding_model = OpenAIEmbeddings()

# Load documents (from local .txt file for example)
documents = load_documents_from_folder("data/sample_docs")
chunks = chunk_documents(documents)


# Chunk the documents
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Embed and index documents with FAISS
vector_store = FAISS.from_documents(chunks, embedding_model)
retriever = vector_store.as_retriever()

# Setup RAG (Retrieval + QA)
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

def ask_rag_question(query: str):
    print("🔎 Querying RAG system...")
    result = rag_chain({"query": query})
    print("✅ Answer:", result['result'])
    print("📚 Sources:")
    for doc in result['source_documents']:
        print("-", doc.metadata.get("source", "Unknown"))

if __name__ == "__main__":
    query = input("❓ Ask a question about the document: ")
    ask_rag_question(query)

