# Time Series Analysis
Python code for implementing statistical tests that identify price series which possess trending, mean-reverting or 
geometric brownian motion (GBM)/random walk behavior.

## (Augmented Dickey-Fuller (ADF) Test)[/ADF.py]
Uses the linear lag model of order p, a model for a time series.
Null hypothesis: The model follows random walk/GBM behavior because the gamma coefficient is 0.
We want to reject null.

## (Hurst Exponent)[/Hurst.py]
Compares the variance of a log price series with the rate of diffusion of the GBM with Hurst Exponent.
If H = 0.5, GMB
If H < 0.5, mean-reverting
If H > 0.5, trending
H near 0, highly mean reverting
H near 1, strongly trending

## (Cointegrated Augmented Dickey-Fuller Test (CADF))[/CADF.py]
For a portfolio of equities. Gets the hedge ratio by performing a linear regression against the two time series and then
tests for stationarity under the linear combination.

## Definitions
**Random Walk**\
A time series sequence of steps in which each step is determined randomly. Most equities behave this way.

**Mean Reverting**\
Follows the Ornstein-Uhlenbeck process. This is to say the change of the price series in the next continuous time
period is proportional to (mean of price - current price + Gaussian noise)

**(Strongly) Stationary**\
The joint probability distribution is invariant. Mean and standard deviation do not change. They diffuse from their 
initial value at a rate slower than GBM/RW.

**Cointegration**\
Picking sets of price series that are stationary and therefore can use mean-reverting strategies. The 2 equities will
have a linear relationship.
