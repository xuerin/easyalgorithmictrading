from statsmodels.tsa.stattools import adfuller
import yfinance as yf

# Download Amazon stock data from Yahoo Finance for the given period
amzn = yf.download("AMZN", start="2000-01-01", end="2015-01-01")

# Debugging: Inspect the DataFrame structure
print(amzn.head())
print(amzn.columns)

# Access the 'Close' column for 'AMZN' in a MultiIndex DataFrame
try:
    close_prices = amzn[('Close', 'AMZN')]
except KeyError:
    raise KeyError("The expected MultiIndex structure is missing or misconfigured.")

# Perform the Augmented Dickey-Fuller test on the 'Close' column
result = adfuller(close_prices, maxlag=1)

# Output the results in a readable format
print("ADF Statistic:", result[0])
print("p-value:", result[1])
print("Critical Values:")
for key, value in result[4].items():
    print(f"   {key}: {value}")

# Interpretation of the test
if result[0] > max(result[4].values()):
    print("\nInterpretation: Since the calculated value of the test statistic is larger than any of the critical values at the 1%, 5%, or 10% levels,"
          "we cannot reject the null hypothesis of γ = 0. Thus, the series is unlikely to be mean-reverting."
          "This aligns with the intuition that most equities behave like Geometric Brownian Motion (GBM), i.e., a random walk.")
else:
    print("\nInterpretation: Since the calculated value of the test statistic is smaller than one or more of the critical values, "
          "we reject the null hypothesis of γ = 0. This suggests the series is mean-reverting.")
