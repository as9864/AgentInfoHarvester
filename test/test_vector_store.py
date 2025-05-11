from infoharvester.news.newsapi import fetch_news_articles
from infoharvester.embeddings.vector_store import NewsVectorStore
from langchain_core.documents import Document

def test_embed_and_query():
    symbol = "AAPL"

    # 1. 뉴스 수집
    articles = fetch_news_articles(symbol, max_articles=5)

    # 2. Document 리스트로 변환
    docs = []
    for a in articles:
        # text = (a.get("title", "") + "\n" + a.get("description", "")).strip()
        title = a.get("title") or ""
        desc = a.get("description") or ""
        text = f"{title}\n{desc}".strip()
        if text:
            docs.append(Document(page_content=text, metadata={"source": "news", "symbol": symbol}))

    # 3. 벡터 저장소 생성 및 저장
    store = NewsVectorStore()
    store.build_index(docs, symbol=symbol)

    # 4. 검색 테스트
    results = store.search("Apple earnings", k=3)
    print("📌 Search Results:")
    for r in results:
        print(f"- {r.page_content.splitlines()[0]}")

if __name__ == "__main__":
    test_embed_and_query()