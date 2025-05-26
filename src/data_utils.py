import yfinance as yf
import pandas as pd 

def get_price_data(tickers, start, end = None, price_type = "Close"):
    """Downlaods historical price data from Yahoo Finance"""
    data = yf.download(tickers, start=start, end=end, progress = False)
    if isinstance(data.columns, pd.MultiIndex):
        prices = data[price_type]
    else:
        prices = data
    return prices.dropna()

def compute_returns(price_df):
    return price_df.pct_change().dropna()

