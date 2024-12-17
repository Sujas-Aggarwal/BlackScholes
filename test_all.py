from logic import BlackScholes
from visualizer import Visualizer
import numpy as np
def test_black_scholes():
    blackScholes = BlackScholes(
        time_to_maturity= 2,
        strike= 90,
        current_price= 100,
        volatility= 0.2,
        interest_rate= 0.05
    )
    call,put= blackScholes.run()
    call = round(call,2)
    put = round(put,2)
    assert call == 22.03 
    assert put == 3.47

def test_visualizer_light():
    spot_range = np.linspace(80, 120, 10)  # Reduced resolution for clarity
    vol_range = np.linspace(0.1, 0.3, 10)
    bs_model = {
        "time_to_maturity": 2,
        "strike": 90,
        "current_price": 100,
        "volatility": 0.2,
        "interest_rate": 0.05
    }
    visualizer = Visualizer()
    visualizer.plot_heatmap(bs_model, spot_range, vol_range, bs_model["strike"])

def test_visualizer_dark():
    spot_range = np.linspace(80, 120, 10)  # Reduced resolution for clarity
    vol_range = np.linspace(0.1, 0.3, 10)
    bs_model = {
        "time_to_maturity": 2,
        "strike": 90,
        "current_price": 100,
        "volatility": 0.2,
        "interest_rate": 0.05
    }
    visualizer = Visualizer()
    visualizer.plot_heatmap(bs_model, spot_range, vol_range, bs_model["strike"],"dark")
