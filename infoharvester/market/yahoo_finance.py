import yfinance as yf
import pandas as pd
from infoharvester.market.indicator_utils import apply_indicators
from datetime import datetime, timedelta

def fetch_price_history(symbol: str, period: str = "30d", interval: str = "1d", include_indicators: bool = True) -> pd.DataFrame:
    """
    Yahoo Finance에서 시세를 가져옴
    :param symbol: 종목 코드 (예: "AAPL")
    :param period: 조회 기간 (예: "30d", "90d", "1y")
    :param interval: 조회 간격 (예: "1d", "1h")
    :return: OHLCV 포함된 DataFrame
    """
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval)
        df = df.rename(columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        }).reset_index()

        # df = df.rename(columns={...}).reset_index()

        if include_indicators:
            df = apply_indicators(df)

        return df
    except Exception as e:
        print(f"❌ Failed to fetch price data for {symbol}: {e}")
        return pd.DataFrame()