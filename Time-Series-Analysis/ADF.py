from statsmodels.tsa.stattools import adfuller
import yfinance as yf


def adf_test(ts, maxlag=1):
    """
    Perform the Augmented Dickey-Fuller (ADF) test on a time series.

    Parameters:
        ts (array-like): The time series to test for stationarity.
        maxlag (int): Maximum number of lags to include in the test.

    Returns:
        dict: A dictionary containing the ADF statistic, p-value, critical values, and interpretation.
    """
    # Perform the ADF test
    result = adfuller(ts, maxlag=maxlag)

    # Prepare the output
    adf_statistic = result[0]
    p_value = result[1]
    critical_values = result[4]
    interpretation = ""

    # Determine interpretation based on the ADF statistic and critical values
    if adf_statistic > max(critical_values.values()):
        interpretation = ("Since the calculated value of the test statistic is larger than any of the critical values "
                          "at the 1%, 5%, or 10% levels, we cannot reject the null hypothesis of γ = 0. "
                          "Thus, the series is unlikely to be mean-reverting. "
                          "This aligns with the intuition that most equities behave like Geometric Brownian Motion (GBM), i.e., a random walk.")
    else:
        interpretation = ("Since the calculated value of the test statistic is smaller than one or more of the critical values, "
                          "we reject the null hypothesis of γ = 0. This suggests the series is mean-reverting.")

    # Return the results as a dictionary
    return {
        "ADF Statistic": adf_statistic,
        "p-value": p_value,
        "Critical Values": critical_values,
        "Interpretation": interpretation
    }


# Download Amazon stock data from Yahoo Finance for the given period
amzn = yf.download("AMZN", start="2000-01-01", end="2015-01-01")

# Access the 'Close' column for 'AMZN' in a MultiIndex DataFrame
try:
    close_prices = amzn[('Close', 'AMZN')] if isinstance(amzn.columns, tuple) else amzn['Close']
except KeyError:
    raise KeyError("The expected MultiIndex structure is missing or misconfigured.")

# Ensure the series has no missing values
close_prices = close_prices.dropna()

# Perform the ADF test using the function
adf_results = adf_test(close_prices.values, maxlag=1)

# Output the results
print(f"ADF Statistic: {adf_results['ADF Statistic']}")
print(f"p-value: {adf_results['p-value']}")
print("Critical Values:")
for key, value in adf_results['Critical Values'].items():
    print(f"   {key}: {value}")
print("\nInterpretation:")
print(adf_results['Interpretation'])
