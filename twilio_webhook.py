# twilio_webhook.py

from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse
from app.ingestion import load_documents_from_folder, chunk_documents
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
import uvicorn

app = FastAPI()

# Load chain (only once)
docs = load_documents_from_folder("data/sample_docs")
chunks = chunk_documents(docs)
embedding_model = OpenAIEmbeddings()
vector_store = FAISS.from_documents(chunks, embedding_model)
retriever = vector_store.as_retriever()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

@app.post("/twilio")
async def whatsapp_webhook(
    request: Request,
    Body: str = Form(...),
    From: str = Form(...)
):
    print(f"📩 Incoming WhatsApp message from {From}: {Body}")
    answer = qa_chain.run(Body)
    return PlainTextResponse(f"{answer}")

if __name__ == "__main__":
    uvicorn.run("twilio_webhook:app", host="0.0.0.0", port=8002, reload=True)

