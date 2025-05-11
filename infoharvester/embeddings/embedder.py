from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

class Embedder:
    def __init__(self, model: str = "text-embedding-ada-002"):
        self.embedding = OpenAIEmbeddings(model=model)

    def embed_documents(self, texts: list) -> list:
        return self.embedding.embed_documents(texts)

    def embed_query(self, query: str) -> list:
        return self.embedding.embed_query(query)