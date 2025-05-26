import matplotlib.pyplot as plt 
import seaborn as sns

def plot_price_trends(prices, title = "Stock Price History", filname = "../plots/price_trends.png"):
    plt.figure(figsize = (12, 6))
    prices.plot(ax = plt.gca()) 
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True) 
    plt.savefig(filname, dpi=300)
    plt.show()

def plot_correlation(returns, title = "Correlation Heatmap", filename = "../plots/corr_heatmap.png"):
    plt.figure(figsize = (10, 8))
    sns.heatmap(returns.corr(), annot = True, cmap = 'coolwarm', fmt = ".2f")
    plt.title(title)
    plt.savefig(filename, dpi=300)
    plt.show()

def plot_cumulative_returns(cum_returns_dict, title = "Cumulative Returns", filename = "../plots/cum_returns"):
    plt.figure(figsize=(12,6))
    for label, series in cum_returns_dict.items():
        series.plot(label=label)
    plt.legend()
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.grid(True) 
    plt.savefig(filename, dpi=300)
    plt.show()

def plot_efficient_frontier(vols, rets, optimal=None, title = "Efficient Frontier", filename = "../plots/eff_frontier.png"):
    plt.figure(figsize=(10,6))
    plt.scatter(vols, rets, c=rets, cmap = 'viridis', alpha = 0.6, label = 'Portfolios')

    if optimal:
        opt_vol, opt_ret = optimal
        plt.scatter(opt_vol, opt_ret, color = 'red', marker = '*', s=200, label = 'Optimal Portfolio')

    plt.xlabel("Volatility")
    plt.ylabel("Expected Return")
    plt.title(title)
    plt.legend()
    plt.grid(True) 
    plt.savefig(filename, dpi=300)
    plt.show()

def plot_weights_bar(weights, labels, title = "Portfolio Allocation", filename = "../plots/port_alloc"):
    plt.figure(figsize=(10,6))
    plt.bar(labels, weights)
    plt.title(title)
    plt.ylabel("Weight")
    plt.xticks(rotation = 45)
    plt.grid(True, axis='y') 
    plt.savefig(filename, dpi=300)
    plt.show()

