from __future__ import print_function
from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn
import yfinance as yf

def hurst(ts):
    """Returns the Hurst Exponent of the time series vector ts"""
    # Create the range of lag values
    lags = range(2, 100)

    # Calculate the array of the variances of the lagged differences
    tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]

    # Use a linear fit to estimate the Hurst Exponent
    poly = polyfit(log(lags), log(tau), 1)

    # Return the Hurst exponent from the polyfit output
    return poly[0] * 2.0

# Generate Example Series
gbm = log(cumsum(randn(100000)) + 1000)  # Geometric Brownian Motion
mr = log(randn(100000) + 1000)           # Mean-Reverting Series
tr = log(cumsum(randn(100000) + 1) + 1000)  # Trending Series

# Output the Hurst Exponent for the example series with interpretation
hurst_gbm = hurst(gbm)
print(f"Hurst(GBM): {hurst_gbm:.4f}")
print("Interpretation: The GBM possesses a Hurst Exponent, H, that is almost exactly 0.5, "
      "indicating random walk behavior.")

hurst_mr = hurst(mr)
print(f"Hurst(MR): {hurst_mr:.4f}")
print("Interpretation: The mean-reverting series has H almost equal to 0, "
      "indicating mean-reverting behavior.")

hurst_tr = hurst(tr)
print(f"Hurst(TR): {hurst_tr:.4f}")
print("Interpretation: The trending series has H close to 1, "
      "indicating strong trending behavior.")

# Download Amazon stock data
amzn = yf.download("AMZN", start="2000-01-01", end="2015-01-01")

# Handle MultiIndex column for 'Close' prices
try:
    amzn_close = amzn[('Close', 'AMZN')] if isinstance(amzn.columns, tuple) else amzn['Close']
except KeyError:
    raise KeyError("Could not find a valid 'Close' column in the DataFrame.")

# Ensure the series has no missing values
amzn_close = amzn_close.dropna()

# Output the Hurst Exponent for Amazon stock prices with interpretation
hurst_amzn = hurst(amzn_close.values)
print(f"Hurst(AMZN): {hurst_amzn:.4f}")
print("Interpretation: Interestingly, Amazon has H close to 0.5, indicating that it behaves "
      "similar to a GBM (random walk), at least for the sample period used.")
