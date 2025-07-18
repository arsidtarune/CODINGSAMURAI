# stock_utils.py
import yfinance as yf
import pandas as pd

def download_stock_data(ticker='AAPL', period='2y'):
    data = yf.download(ticker, period=period)
    data = data[['Close']]  # Only closing price
    data.dropna(inplace=True)
    return data

def prepare_data(data, window_size=5):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i + window_size].flatten())

        y.append(data[i + window_size])
    return pd.DataFrame(X), pd.Series(y)
