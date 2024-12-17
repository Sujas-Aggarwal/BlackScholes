from logic import BlackScholes
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def plot_heatmap(bs_model, spot_range, vol_range, strike):
    call_prices = np.zeros((len(vol_range), len(spot_range)))
    put_prices = np.zeros((len(vol_range), len(spot_range)))
    
    for i, vol in enumerate(vol_range):
        for j, spot in enumerate(spot_range):
            blackScholes = BlackScholes(
                time_to_maturity=bs_model["time_to_maturity"],
                strike=strike,
                current_price=spot,
                volatility=vol,
                interest_rate=bs_model["interest_rate"]
            )
            call_prices[i, j], put_prices[i, j] = blackScholes.run()
    fig_call, ax_call = plt.subplots(figsize=(10, 8))
    sns.heatmap(call_prices, xticklabels=np.round(spot_range, 2), yticklabels=np.round(vol_range, 2), annot=True, fmt=".2f", cmap="viridis", ax=ax_call)
    ax_call.set_title('CALL')
    ax_call.set_xlabel('Spot Price')
    ax_call.set_ylabel('Volatility')
    
    # Plotting Put Price Heatmap
    fig_put, ax_put = plt.subplots(figsize=(10, 8))
    sns.heatmap(put_prices, xticklabels=np.round(spot_range, 2), yticklabels=np.round(vol_range, 2), annot=True, fmt=".2f", cmap="viridis", ax=ax_put)
    ax_put.set_title('PUT')
    ax_put.set_xlabel('Spot Price')
    ax_put.set_ylabel('Volatility')
    
    return fig_call, fig_put

if __name__ == '__main__':
    spot_range = np.linspace(80, 120, 10)  # Reduced resolution for clarity
    vol_range = np.linspace(0.1, 0.3, 10)
    bs_model = {
        "time_to_maturity": 2,
        "strike": 90,
        "current_price": 100,
        "volatility": 0.2,
        "interest_rate": 0.05
    }
    fig_call, fig_put = plot_heatmap(bs_model, spot_range, vol_range, bs_model["strike"])
    fig_call.show()
    fig_put.show()
    plt.show()
