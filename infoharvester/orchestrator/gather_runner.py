import os
from infoharvester.news.newsapi import fetch_news_articles
from infoharvester.fundamentals.finhub_api import fetch_company_profile, fetch_financials
from infoharvester.market.yahoo_finance import fetch_price_history
from infoharvester.embeddings.vector_store import NewsVectorStore
from langchain_core.documents import Document
from utils.config_loader import load_config
import yaml



def build_documents(symbol: str, news: list, profile: dict, financials: dict) -> list:
    docs = []

    # 📄 뉴스 문서
    for a in news:
        # text = (a.get("title", "") + "\n" + a.get("description", "")).strip()
        title = a.get("title") or ""
        desc = a.get("description") or ""
        text = f"{title}\n{desc}".strip()
        if text:
            docs.append(Document(page_content=text, metadata={"source": "news", "symbol": symbol}))

    # 🧾 펀더멘털 문서
    if profile:
        profile_text = "\n".join([
            f"Company: {profile.get('name', '')}",
            f"Sector: {profile.get('finnhubIndustry', '')}",
            f"CEO: {profile.get('ceo', '')}",
            f"Website: {profile.get('weburl', '')}"
        ])
        docs.append(Document(page_content=profile_text, metadata={"source": "profile", "symbol": symbol}))

    if financials:
        fin_text = "\n".join([
            f"Revenue/Share: {financials.get('revenuePerShareTTM', 'N/A')}",
            f"Net Margin: {financials.get('netProfitMarginTTM', 'N/A')}",
            f"ROE: {financials.get('roeTTM', 'N/A')}",
            f"Debt/Equity: {financials.get('totalDebt/totalEquity', 'N/A')}"
        ])
        docs.append(Document(page_content=fin_text, metadata={"source": "financials", "symbol": symbol}))

    return docs

def run_full_pipeline(symbol: str):
    print(f"📡 Gathering data for {symbol}...")

    # 1. 수집
    news = fetch_news_articles(symbol, max_articles=5)
    profile = fetch_company_profile(symbol)
    financials = fetch_financials(symbol)
    price_df = fetch_price_history(symbol, period="60d")

    # 2. 문서 구성
    docs = build_documents(symbol, news, profile, financials)

    # 3. 벡터 저장
    print(f"💾 Saving {len(docs)} documents to FAISS index...")
    store = NewsVectorStore()
    store.build_index(docs, symbol=symbol)

    print(f"✅ Vector index saved for {symbol}!")

    # (선택) 마켓 데이터 저장

    config = load_config()
    raw_path = config["paths"]["raw_path"]

    market_path = f"market_{symbol}.csv"
    market_path = raw_path+market_path
    os.makedirs(os.path.dirname(market_path), exist_ok=True)
    price_df.to_csv(market_path, index=False)
    print(f"📈 Market data saved: {market_path}")

if __name__ == "__main__":
    run_full_pipeline("AAPL")