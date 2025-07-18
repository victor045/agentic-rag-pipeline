# test_rag.py

import unittest
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.schema import Document

class TestRAGPipeline(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup test documents
        docs = [
            Document(page_content="LangChain is a framework for building LLM applications."),
            Document(page_content="FAISS is a library for efficient similarity search."),
        ]

        # Embeddings and retriever
        embeddings = OpenAIEmbeddings()
        cls.vector_store = FAISS.from_documents(docs, embeddings)
        cls.retriever = cls.vector_store.as_retriever()
        cls.qa_chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(temperature=0), retriever=cls.retriever)

    def test_basic_query(self):
        result = self.qa_chain.run("What is LangChain?")
        self.assertIn("LangChain", result)

    def test_similar_doc_retrieval(self):
        results = self.retriever.get_relevant_documents("similarity search")
        self.assertGreater(len(results), 0)
        self.assertIn("FAISS", results[0].page_content)

    def test_no_match(self):
        result = self.qa_chain.run("Tell me about zebras in space.")
        self.assertTrue(isinstance(result, str))
        self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()

