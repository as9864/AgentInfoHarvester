from infoharvester.news.newsapi import fetch_news_articles

def test_fetch_news():
    articles = fetch_news_articles("Apple Inc", max_articles=5)
    for a in articles:
        print(f"[{a['publishedAt']}] {a['title']}")
        print(f"→ {a['description']}\n")

if __name__ == "__main__":
    test_fetch_news()