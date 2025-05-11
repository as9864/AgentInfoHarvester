import os
import requests
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 API 키 로딩

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"


def fetch_news_articles(query: str, max_articles: int = 10) -> List[Dict]:
    if not NEWS_API_KEY:
        raise ValueError("Missing NEWS_API_KEY in environment variables.")

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": max_articles,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_API_ENDPOINT, params=params)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch news: {response.status_code}, {response.text}")

    data = response.json()
    return data.get("articles", [])