# streamlit_app.py

import streamlit as st
from app.ingestion import load_documents_from_folder, chunk_documents
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

st.set_page_config(page_title="Agentic RAG Chat", layout="centered")
st.title("🧠 Agentic RAG System")

# Load and index documents only once
@st.cache_resource
def load_chain():
    docs = load_documents_from_folder("data/sample_docs")
    chunks = chunk_documents(docs)
    embeddings = OpenAIEmbeddings()
    store = FAISS.from_documents(chunks, embeddings)
    retriever = store.as_retriever()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return chain

qa_chain = load_chain()

# Input and response
query = st.text_input("Ask a question about your documents:", placeholder="e.g. What does the privacy policy say?")

if query:
    with st.spinner("Thinking..."):
        result = qa_chain({"query": query})
        st.success(result["result"])

        with st.expander("📚 View sources"):
            for doc in result["source_documents"]:
                st.markdown(f"- {doc.metadata.get('source', 'unknown')}")

