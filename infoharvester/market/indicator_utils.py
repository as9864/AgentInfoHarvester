import pandas as pd

def calculate_sma(df: pd.DataFrame, window: int = 5) -> pd.Series:
    return df["close"].rolling(window=window).mean()

def calculate_rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    delta = df["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


# def apply_indicators(df: pd.DataFrame) -> pd.DataFrame:
#     df = df.copy()
#     # print("applying indicators : df", df)
#     df["SMA_5"] = calculate_sma(df, window=5)
#     # print("applying indicators : df2", df)
#     df["RSI_14"] = calculate_rsi(df, period=14)
#     # print("applying indicators : df3", df)
#     return df

def apply_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["SMA_5"] = df["close"].rolling(window=5).mean()
    df["RSI_14"] = calculate_rsi(df["close"], period=14)
    return df

def calculate_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    # print("delta", delta)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    # print("gain : ", gain)
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    # print("loss : " , loss)
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi