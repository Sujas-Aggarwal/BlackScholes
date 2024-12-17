from numpy import exp, sqrt, log
from scipy.stats import norm


# This Logic of BlackScholes Algo is inspired from - https://github.com/prudhvi-reddy-m/BlackScholes
# Its very simple and easy to understand, the code is pretty much self explanatory, I think.
class BlackScholes:
    def __init__(
        self,
        time_to_maturity: float,
        strike: float,
        current_price: float,
        volatility: float,
        interest_rate: float,
    ):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.current_price = current_price
        self.volatility = volatility
        self.interest_rate = interest_rate

    def run(
        self,
    ):
        time_to_maturity = self.time_to_maturity
        strike = self.strike
        current_price = self.current_price
        volatility = self.volatility
        interest_rate = self.interest_rate

        d1 = (
            log(current_price / strike) +
            (interest_rate + 0.5 * volatility ** 2) * time_to_maturity
            ) / (
                volatility * sqrt(time_to_maturity)
            )
        d2 = d1 - volatility * sqrt(time_to_maturity)

        call_price = current_price * norm.cdf(d1) - (
            strike * exp(-(interest_rate * time_to_maturity)) * norm.cdf(d2)
        )
        put_price = (
            strike * exp(-(interest_rate * time_to_maturity)) * norm.cdf(-d2)
        ) - current_price * norm.cdf(-d1)

        self.call_price = call_price
        self.put_price = put_price
        self.call_delta = norm.cdf(d1)
        self.put_delta = 1 - norm.cdf(d1)
        self.call_gamma = norm.pdf(d1) / (
            strike * volatility * sqrt(time_to_maturity)
        )
        self.put_gamma = self.call_gamma
        return call_price,put_price

# For Manual Unit Testing
if __name__ == "__main__":
    blackScholes = BlackScholes(
        time_to_maturity= 2,
        strike= 90,
        current_price= 100,
        volatility= 0.2,
        interest_rate= 0.05
    )
    call,put= blackScholes.run()
    print(f"Call Value = {round(call,2)}\nPut Value = {round(put,2)}")
