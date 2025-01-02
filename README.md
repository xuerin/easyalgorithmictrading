# Time Series Analysis
Python code for implementing statistical tests that identify price series that possess trending, mean-reverting or 
geometric brownian motion (GBM)/random walk behavior.

## [Augmented Dickey-Fuller (ADF) Test](ADF.py)
Uses the linear lag model of order p, a model for a time series.
Null hypothesis: The model follows random walk/GBM behavior because the gamma coefficient is 0.
We want to reject null.

## [Hurst Exponent](Hurst.py)
Compares the variance of a log price series with the rate of diffusion of the GBM with Hurst Exponent.
$$Var(\tau) = <|log(t+\tau) - log(t)|^2>$$
$$<|log(t+\tau) - log(t)|^2> ~{\tau}^{2H}$$
If $H = 0.5$, GMB\
If $H < 0.5$, mean-reverting\
If $H > 0.5$, trending\
H near 0, highly mean reverting\
H near 1, strongly trending\

## [Cointegrated Augmented Dickey-Fuller Test (CADF)](CADF.py)
For a portfolio of equities. Gets the hedge ratio by performing a linear regression against the two time series and then
tests for stationarity under the linear combination.

## Definitions
**Random Walk**\
A time series sequence of steps in which each step is determined randomly. Most equities behave this way.
$$X_t = X_{t-1}+ {\epsilon}_t$$
$X_{t-1}$ is the position at previous time step\
${\epsilon}_t$ is a random step at $t$ from a probability distribution.

**Mean Reverting**\
Follows the Ornstein-Uhlenbeck process. This is to say the change of the price series in the next continuous time
period is proportional to (mean of price - current price + Gaussian noise).
$$dx_t = \theta \(\mu - x_t\)dt + \delta dW_t$$
$\mu$ is the mean\
$\delta$ is the variance\
$\theta$ is the rate of reversion to mean\
$W_t$ is the Wiener Process/Brownian Motion

**(Strongly) Stationary**\
The joint probability distribution is invariant. Mean and standard deviation do not change. They diffuse from their 
initial value at a rate slower than GBM/RW.

**Cointegration**\
Picking sets of price series that are stationary and therefore can use mean-reverting strategies. The 2 equities will
have a linear relationship.
$$ y(t) = \Beta x(t) + {\epsilon}(t)$$
$y(t), x(t)$ is the price of equity y, x respectively on day $t$\
${\epsilon}(t)$ is the residual. 
