import numpy as np 
from scipy.optimize import minimize 

def get_bounds(n_assets, allow_short):
    """Returns tuple of bounds depending on whether short-selling is allowed."""
    return tuple((-1, 1) if allow_short else (0, 1) for _ in range(n_assets)) 

#1. Max Sharpe
def optimize_sharpe(mean_returns, cov_matrix, risk_free_rate = 0.045, allow_short = False):
    n_assets = len(mean_returns)

    # Objective function: negative Sharpe ratio
    def neg_sharpe(weights):
        ret = np.dot(weights, mean_returns)
        vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        return -(ret - risk_free_rate) / vol

    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1}) # weights sum up to 0 
    bounds = get_bounds(n_assets, allow_short)

    init_guess = np.repeat(1 / n_assets, n_assets) #starting point for optimization

    result = minimize(neg_sharpe, init_guess, bounds = bounds, constraints = constraints, method = 'SLSQP')

    return result.x 

#2. Min Variance
def minimize_variance(cov_matrix, allow_short = False):
    n_assets = cov_matrix.shape[0]

    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    
    bounds = get_bounds(n_assets, allow_short)
    constraints = {'type':'eq', 'fun': lambda x: np.sum(x) - 1}
    init_guess = np.repeat(1 / n_assets, n_assets)

    result = minimize(portfolio_volatility, init_guess, bounds = bounds, constraints = constraints, method = 'SLSQP')

    return result.x

#3. Target Return
def target_return_portfolio(mean_returns, cov_matrix, target_return, allow_short = False):
    n_assets = len(mean_returns)

    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    
    bounds = get_bounds(n_assets, allow_short)
    constraints = (
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
        {'type': 'eq', 'fun': lambda x: np.dot(x, mean_returns) - target_return}

    )
    init_guess = np.repeat(1 / n_assets, n_assets)
    
    result = minimize(portfolio_volatility, init_guess, bounds = bounds, constraints = constraints, method = 'SLSQP')

    return result.x

#4. Risk Parity
def risk_parity_portfolio(cov_matrix, allow_short = False):
    n_assets = cov_matrix.shape[0]

    def risk_contribution(weights):
        port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        marginal_contrib = np.dot(cov_matrix, weights)
        risk_contrib = weights * marginal_contrib / port_vol
        return risk_contrib
    
    def objective(weights):
        rc = risk_contribution(weights)
        return np.sum((rc - np.mean(rc)) ** 2) #variance of contributions
    
    bounds = get_bounds(n_assets, allow_short)
    constraints = {'type':'eq', 'fun': lambda x: np.sum(x) - 1}
    init_guess = np.repeat(1 / n_assets, n_assets)

    result = minimize(objective, init_guess, bounds = bounds, constraints=constraints, method = 'SLSQP')

    return result.x

#5. Efficient Frontier

def efficient_frontier(mean_returns, cov_matrix, n_points = 50, allow_short = False):
    min_ret = np.min(mean_returns)
    max_ret = np.max(mean_returns) * 1.25
    target_returns = np.linspace(min_ret, max_ret, n_points)

    frontier = []
    for target in target_returns:
        try: 
            weights = target_return_portfolio(mean_returns, cov_matrix, target, allow_short)
            vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            frontier.append((vol, target, weights))
        except: 
            continue 
    return frontier
    
