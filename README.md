# Black-Scholes Pricing Model

The **Black-Scholes model** is a mathematical framework used to price options. Developed by **Fischer Black**, **Myron Scholes**, and **Robert Merton**, this model provides a theoretical estimate for the price of **European-style options**. It assumes constant volatility of the underlying asset and no dividends during the option's lifetime.

---

## Formula

The price of a **call option** under the Black-Scholes model is calculated as:

\[
C = S_0 N(d_1) - X e^{-rT} N(d_2)
\]

### Where:

- \( C \): Price of the call option
- \( S_0 \): Current price of the underlying asset
- \( X \): Strike price of the option
- \( r \): Risk-free interest rate
- \( T \): Time to maturity (in years)
- \( N(\cdot) \): Cumulative distribution function of the standard normal distribution
- \( \sigma \): Volatility of the underlying asset

---

## Intermediate Variables

The values \( d_1 \) and \( d_2 \) are calculated as follows:

\[
d_1 = \frac{\ln(S_0 / X) + (r + \sigma^2 / 2) T}{\sigma \sqrt{T}}
\]

\[
d_2 = d_1 - \sigma \sqrt{T}
\]

---

## Key Assumptions of the Model

1. The option is European-style (exercisable only at maturity).
2. No dividends are paid during the option's life.
3. The volatility (\( \sigma \)) of the underlying asset is constant.
4. The risk-free interest rate (\( r \)) is constant.
5. The returns of the underlying asset follow a **log-normal distribution**.
6. Markets are frictionless (no transaction costs or taxes).

---

## Applications

The Black-Scholes model is widely used in:

- **Option pricing**: Valuation of call and put options.
- **Risk management**: Hedging strategies for portfolios.
- **Financial derivatives**: Foundation for various derivative pricing models.

Despite its assumptions and limitations, the Black-Scholes model remains a cornerstone of **quantitative finance**.

---

## Limitations

While the model is widely applicable, it has limitations:

- Assumes constant volatility and interest rates.
- Not suitable for options on assets paying dividends without adjustments.
- Does not account for market frictions like transaction costs.
- Only applicable to European options.
