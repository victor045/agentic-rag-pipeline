# api_main.py

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from app.ingestion import load_documents_from_folder, chunk_documents
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

app = FastAPI(title="Agentic RAG API")

# Load and index documents
folder_path = "data/sample_docs"
documents = load_documents_from_folder(folder_path)
chunks = chunk_documents(documents)
embedding_model = OpenAIEmbeddings()
vector_store = FAISS.from_documents(chunks, embedding_model)
retriever = vector_store.as_retriever()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

class QueryRequest(BaseModel):
    question: str

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/ask")
def ask_question(req: QueryRequest):
    result = qa_chain({"query": req.question})
    return {
        "question": req.question,
        "answer": result["result"],
        "sources": [doc.metadata.get("source", "unknown") for doc in result["source_documents"]]
    }

