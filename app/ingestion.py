# ingestion.py

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import os
from typing import List

def load_documents_from_folder(folder_path: str):
    documents = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".txt"):
            loader = TextLoader(file_path)
            documents.extend(loader.load())

        elif filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

        else:
            print(f"⚠️ Skipping unsupported file: {filename}")

    return documents


def chunk_documents(documents: List[Document], chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(documents)
    return chunks


def ingest_folder(folder_path: str):
    print(f"📂 Loading documents from: {folder_path}")
    docs = load_documents_from_folder(folder_path)
    print(f"📄 Loaded {len(docs)} documents.")

    print("🔪 Chunking documents...")
    chunks = chunk_documents(docs)
    print(f"✅ Generated {len(chunks)} chunks.")

    for i, c in enumerate(chunks[:3]):
        print(f"--- Chunk {i+1} ---\n{c.page_content[:200]}...\n")

    return chunks


if __name__ == "__main__":
    ingest_folder("data/sample_docs")

