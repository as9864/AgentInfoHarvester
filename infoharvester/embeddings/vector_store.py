import os
# # from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
# # from langchain.schema import Document

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from utils.config_loader import load_config
import os


class NewsVectorStore:
    def __init__(self, index_path: str = None):
        if index_path is None:
            config = load_config()
            index_path = config["paths"]["faiss_index"]

        self.index_path = index_path
        self.embedding = OpenAIEmbeddings()
        self.vectorstore = None

    def build_index(self, docs: list, symbol: str = "UNKNOWN"):
        self.vectorstore = FAISS.from_documents(docs, self.embedding)
        self.vectorstore.save_local(self.index_path)

    def load_index(self):
        self.vectorstore = FAISS.load_local(self.index_path, self.embedding, allow_dangerous_deserialization=True)

    def search(self, query: str, k: int = 3):
        if not self.vectorstore:
            self.load_index()
        return self.vectorstore.similarity_search(query, k=k)