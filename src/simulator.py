import numpy as np 
import pandas as pd 
import yfinance as yf 
import matplotlib.pyplot as plt
from datetime import datetime
import os 
from src.data_utils import get_price_data

def simulate_portfolio(tickers, weights, investment_date, end_date = None, plot = True, save_path = None, log_path = None):
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")
    
    prices = get_price_data(tickers, start = investment_date, end=end_date)

    # price = $1 on investment day
    normed = prices / prices.iloc[0]

    # simulated portfolio value over time
    portfolio_value = (normed * weights).sum(axis = 1)

    # save daily log 
    if log_path:
        log_df = pd.DataFrame({"Portfolio Value": portfolio_value})
        log_df.to_csv(log_path, index = True)

    if plot:
        plt.figure(figsize=(12, 6))
        portfolio_value.plot(label="Simulated Portfolio")
        plt.axhline(1.0, linestyle='--', color='gray', label='Initial Investment ($1)')
        plt.title("Simulated Portfolio Value Since Investment Date")
        plt.ylabel("Portfolio Value ($)")
        plt.xlabel("Date")
        plt.grid(True)
        plt.legend()
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()

    return portfolio_value


def simulate_asset_contributions(tickers, weights, investment_date, end_date=None, plot=True, log_path=None, save_path=None):
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")

    prices = get_price_data(tickers, start=investment_date, end=end_date)
    normed = prices / prices.iloc[0]
    
    contributions = normed * weights # asset contributions

    if log_path:
        contributions.to_csv(log_path, index = True)

    if plot:
        contributions.plot(figsize = (12, 6), title = "Asset-Level Portfolio Contribution")
        plt.ylabel("Scaled Contribution")
        plt.grid(True)
        plt.tight_layout()

        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()

    return contributions

