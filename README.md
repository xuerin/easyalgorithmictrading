# Time Series Analysis

Python code for implementing statistical tests that identify price series that possess trending, mean-reverting, or geometric Brownian motion (GBM)/random walk behavior.

---

## [Augmented Dickey-Fuller (ADF) Test](ADF.py)
**Purpose**: Tests for stationarity in a time series using a linear lag model of order $p$, where the change in the value of the time series is proportional to:
  - A constant.
  - A temporal trend.
  - Previous $p$-values.
  - An error term.

$$
\Delta y_t = \alpha + \beta t + \gamma y_{t-1} + \delta_1 \Delta y_{t-1} + \cdots + \delta_{p-1} \Delta y_{t-p+1} + \epsilon_t
$$

- $\Delta y_t$: The first difference of the series, $\Delta y_t = y(t) - y(t-1)$.
- $\alpha$: A constant.
- $\beta$: The coefficient of a temporal trend.
- $\gamma$: The coefficient of $y_{t-1}$, used to test for stationarity.
- $\delta_1, \delta_2, \dots, \delta_{p-1}$: Coefficients for the lagged differences of the series.
- $\epsilon_t$: The error term.

**Null Hypothesis ($H_0$)**: The time series follows a random walk (non-stationary), which implies $\gamma = 0$.
**Objective**: Reject the null hypothesis to conclude that the time series is stationary/mean-reverting and does not follow a random walk.

---

## [Hurst Exponent](Hurst.py)
**Purpose**: Compares the variance of a log price series with the rate of diffusion of GBM using the Hurst exponent.

$$
\text{Var}(\tau) = \langle | \log(t+\tau) - \log(t) |^2 \rangle
$$

$$
\langle | \log(t+\tau) - \log(t) |^2 \rangle \sim \tau^{2H}
$$

### **Interpretation**:
- If $H = 0.5$: GBM (Random Walk).
- If $H < 0.5$: Mean-reverting behavior.
- If $H > 0.5$: Trending behavior.
- $H$ near $0$: Highly mean-reverting.
- $H$ near $1$: Strongly trending.

---

## [Cointegrated Augmented Dickey-Fuller Test (CADF)](CADF.py)
**Purpose**: Tests for stationarity in a portfolio of equities.
**Process**:
1. Compute the hedge ratio by performing a linear regression between the two time series.
2. Test for stationarity of the residuals (linear combination) using the ADF test.

---

## Definitions

### **Random Walk**
A time series sequence of steps where each step is determined randomly. Most equities behave this way.

$$
X_t = X_{t-1} + \epsilon_t
$$

- $X_{t-1}$: Position at the previous time step.
- $\epsilon_t$: Random step at $t$, drawn from a probability distribution.

---

### **Mean-Reverting**
A mean-reverting series follows the Ornstein-Uhlenbeck process, where the change in the price series in the next continuous time period is proportional to:

$$
dx_t = \theta (\mu - x_t) dt + \delta dW_t
$$

- $\mu$: Mean value.
- $\delta$: Variance.
- $\theta$: Rate of reversion to the mean.
- $W_t$: Wiener Process/Brownian Motion.

---

### **(Strongly) Stationary**
A time series is stationary if its joint probability distribution is invariant over time. This means:
- The mean and standard deviation remain constant.
- The rate of diffusion is slower than GBM/random walk.

---

### **Cointegration**
Cointegration involves selecting pairs of price series that, while individually non-stationary, exhibit a stationary linear combination. This allows for mean-reverting trading strategies.

$$
y(t) = \beta x(t) + \epsilon(t)
$$

- $y(t), x(t)$: Prices of equities $y$ and $x$ at time $t$.
- $\beta$: Hedge ratio.
- $\epsilon(t)$: Residuals of the linear relationship.
