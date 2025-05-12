import os
import pandas as pd
from utils.config_loader import load_config

def load_price_data(symbol: str) -> pd.DataFrame:
    config = load_config()
    raw_path = config["paths"]["raw_path"]

    market_path = f"market_{symbol}.csv"
    path = raw_path + market_path

    # path = f"storage/raw_data/market_{symbol}.csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"No price data for {symbol}")
    return pd.read_csv(path)