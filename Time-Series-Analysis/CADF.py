import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.regression.linear_model import OLS
from statsmodels.tsa.stattools import adfuller
import pprint


def plot_price_series(df, ts1, ts2):
    """Plot the price histories of two stocks."""
    months = mdates.MonthLocator()  # every month
    fig, ax = plt.subplots()
    ax.plot(df.index, df[ts1], label=ts1)
    ax.plot(df.index, df[ts2], label=ts2)
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.set_xlim(datetime.datetime(2012, 1, 1), datetime.datetime(2013, 1, 1))
    ax.grid(True)
    fig.autofmt_xdate()
    plt.xlabel('Month/Year')
    plt.ylabel('Price ($)')
    plt.title(f'{ts1} and {ts2} Daily Prices')
    plt.legend()
    plt.show()


def plot_scatter_series(df, ts1, ts2):
    """Plot the scatter plot of two stocks' prices."""
    plt.scatter(df[ts1], df[ts2])
    plt.xlabel(f'{ts1} Price ($)')
    plt.ylabel(f'{ts2} Price ($)')
    plt.title(f'{ts1} and {ts2} Price Scatterplot')
    plt.show()


def plot_residuals(df):
    """Plot the residuals."""
    months = mdates.MonthLocator()  # every month
    fig, ax = plt.subplots()
    ax.plot(df.index, df["res"], label="Residuals")
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.set_xlim(datetime.datetime(2012, 1, 1), datetime.datetime(2013, 1, 1))
    ax.grid(True)
    fig.autofmt_xdate()
    plt.xlabel('Month/Year')
    plt.ylabel('Price ($)')
    plt.title('Residual Plot')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Define the time period
    start = datetime.datetime(2012, 1, 1)
    end = datetime.datetime(2013, 1, 1)

    # Download stock data from Yahoo Finance
    xom = yf.download("XOM", start=start, end=end)  # Exxon Mobil
    cvx = yf.download("CVX", start=start, end=end)  # Chevron

    # Print the columns to verify structure
    print(xom.head())
    print(xom.columns)
    print(cvx.head())
    print(cvx.columns)

    # Safely access the 'Adj Close' or 'Close' column
    df = pd.DataFrame(index=xom.index)
    df["XOM"] = xom["Adj Close"] if "Adj Close" in xom.columns else xom["Close"]
    df["CVX"] = cvx["Adj Close"] if "Adj Close" in cvx.columns else cvx["Close"]

    # Plot the two time series
    plot_price_series(df, "XOM", "CVX")

    # Display a scatter plot of the two time series
    plot_scatter_series(df, "XOM", "CVX")

    # Calculate optimal hedge ratio "beta" using OLS
    x = df["XOM"].values.reshape(-1, 1)
    y = df["CVX"].values
    model = OLS(y, x).fit()
    beta_hr = model.params[0]

    # Calculate the residuals of the linear combination
    df["res"] = df["CVX"] - beta_hr * df["XOM"]

    # Plot the residuals
    plot_residuals(df)

    # Perform the Cointegrated Augmented Dickey-Fuller (CADF) test on the residuals
    cadf = adfuller(df["res"].dropna())
    test_statistic = cadf[0]
    p_value = cadf[1]
    critical_values = cadf[4]
    critical_5 = critical_values["5%"]

    # Print CADF Test Results
    print("CADF Test Results:")
    pprint.pprint({
        "Test Statistic": test_statistic,
        "p-value": p_value,
        "Critical Values": critical_values
    })

    # Interpretation of the test
    if test_statistic < critical_5:
        print(f"\nIt can be seen that the calculated test statistic ({test_statistic:.4f}) is smaller than the 5% critical value ({critical_5:.4f}), "
            "which means that we can reject the null hypothesis that there isn’t a cointegrating relationship at the 5% level. "
            "Hence we can conclude, with a reasonable degree of certainty, that XOM and CVX possess a cointegrating relationship, "
            "at least for the time period sample considered.")
    else:
        print(f"\nIt can be seen that the calculated test statistic ({test_statistic:.4f}) is larger than the 5% critical value ({critical_5:.4f}), "
            "which means that we cannot reject the null hypothesis that there isn’t a cointegrating relationship at the 5% level. "
            "Hence we cannot conclude, with a reasonable degree of certainty, that XOM and CVX possess a cointegrating relationship, "
            "at least for the time period sample considered.")
