import yfinance as yf 
import os 
from datetime import datetime

def get_news_for_ticker(ticker, limit = 3):
    """
    Retrieves the most recent news headlines for a given stock tiker.

    Parameters:
        ticker (str): Stock symbol
        limit (int): Number of top news headlines to return

    Returns:
        list of dics: Each containing 'title', 'publisher', 'link', 'providerPublishTime'
    """
    try:
        stock = yf.Ticker(ticker)
        return stock.news[:limit]
    except Exception as e:
        print(f"Error retrieving news for {ticker}: {e}")
        return []
    
def summarize_news(tickers, limit=3, save_path = None):
    """
    Retrieves and formats news for a list of tickers. Optionally saves to a markdown file.

    Parameters:
        tickers (list): List of stock tickers
        limit (int): Number of headlines per stock
        save_path (str): If provided, saves the output as a markdown file

    Returns:
        str: Formatted news summary (markdown-style)
    """

    output = [f"# Potfolio News Summary ({datetime.today().date()})\n"]

    for ticker in tickers:
        output.append(f"\n## {ticker} News:")
        news_items = get_news_for_ticker(ticker, limit)
        valid_found = False

        for i, item in enumerate(news_items):
            content = item.get("content", {})
            title = content.get("title")

            link = content.get("clickThroughUrl", {}).get("url") if isinstance(content.get("clickThroughUrl"), dict) else None

            provider = content.get("provider", {})
            publisher = provider.get("displayName", "Unknown")
    
            #print(f"{ticker} - Item {i}: title={title}, link={link}, publisher={publisher}")
                  
            if title and link:
                output.append(f"- [{title}]({link}) — *{publisher}*")
                valid_found = True

        if not valid_found: 
            output.append("- No recent headlines found.")
    
    summary = "\n".join(output)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(summary)
    
    return summary 