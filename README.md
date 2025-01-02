# Time Series Analysis
Python code for implementing statistical tests that identify price series which possess trending, mean-reverting or GBM
behavior.

## Augmented Dickey-Fuller (ADF) Test
Uses the linear lag model of order p, a model for a time series.
Null hypothesis: The model follows random walk/GBM behavior because the gamma coefficient is 0.
We want to reject null.

## Hurst Exponent
Compares the variance of a log price series with the rate of diffusion of the GBM with Hurst Exponent.
If H = 0.5, GMB
If H < 0.5, mean-reverting
If H > 0.5, trending
H near 0, highly mean reverting
H near 1, strongly trending

## Cointegrated Augmented Dickey-Fuller Test (CADF)
Gets the hedge ratio by performing a linear regression against the two time series and then
tests for stationarity under the linear combination.


