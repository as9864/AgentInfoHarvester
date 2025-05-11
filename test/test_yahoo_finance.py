from infoharvester.market.yahoo_finance import fetch_price_history

def test_indicators():
    df = fetch_price_history("AAPL", period="60d")
    # print(df)
    print(df[["close", "SMA_5", "RSI_14"]].tail())

if __name__ == "__main__":
    test_indicators()