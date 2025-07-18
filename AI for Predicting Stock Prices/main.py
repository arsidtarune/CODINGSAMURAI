# main.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from stock_utils import download_stock_data, prepare_data
import matplotlib.pyplot as plt

# Step 1: Download data
data = download_stock_data('AAPL', '1y')
prices = data['Close'].values

# Step 2: Prepare time series data
window_size = 5
X, y = prepare_data(prices, window_size)
X_train, X_test = X[:200], X[200:]
y_train, y_test = y[:200], y[200:]

# Step 3: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predict and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse:.2f}')

# Step 5: Plot results
plt.plot(range(len(y_test)), y_test, label='Actual')
plt.plot(range(len(predictions)), predictions, label='Predicted')
plt.legend()
plt.title("Stock Price Prediction")
plt.show()
