import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")
BASE_URL = "https://finnhub.io/api/v1"

def fetch_company_profile(symbol: str) -> dict:
    url = f"{BASE_URL}/stock/profile2?symbol={symbol}&token={API_KEY}"
    res = requests.get(url)
    return res.json()

def fetch_financials(symbol: str) -> dict:
    url = f"{BASE_URL}/stock/metric?symbol={symbol}&metric=all&token={API_KEY}"
    res = requests.get(url)
    return res.json().get("metric", {})