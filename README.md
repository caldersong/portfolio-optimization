# Portfolio Optimization with Real-Time Insights

This project combines classical portfolio optimization with real-time simulation and live news-based analysis. It models realistic investing behavior: construct a portfolio using historical data, simulate post-investment performance, and stay updated with relevant market-moving news.


## What This Project Does

- Uses historical stock data to optimize portfolio weights based on:
  - Sharpe ratio
  - Minimum variance
  - Target return
  - Risk parity
- Tracks portfolio value after a user-defined investment date
- Visualizes asset-level contributions and benchmark comparisons
- Pulls recent news headlines for each stock to contextualize performance
- Saves charts and logs automatically to the `plots/` folder


## 📁 Folder Structure

```
portfolio-optimization/
├── src/
│   ├── data_utils.py         # Historical price fetching + returns
│   ├── optimizer.py          # Optimization logic
│   ├── plot_utils.py         # Visualization functions
│   ├── simulator.py          # Simulated investment tracking
│   └── news_utils.py         # Real-time news headline extraction
├── notebooks/
│   └── analysis.ipynb        # Main analysis notebook
├── plots/
│   ├── simulated_portfolio.png
│   ├── asset_contributions.png
│   └── news_YYYY-MM-DD.md
├── requirements.txt
└── README.md
```

## Highlights

- Optimization via Sharpe ratio, min variance, risk parity, and target return
- Simulated post-investment performance
- Asset-level contribution tracking
- Real-time news insight for each ticker
- Auto-logged markdown + image outputs

## Future Extensions

- Add monthly/quarterly rebalancing
- Deploy as an interactive Streamlit dashboard
- Integrate sentiment or earnings data
- Export results to PDF or dashboard reports


