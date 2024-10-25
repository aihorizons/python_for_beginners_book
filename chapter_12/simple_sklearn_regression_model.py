from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

# Load a dataset (using Pandas)
data = pd.read_csv('data.csv')
X = data[['feature1', 'feature2']]
y = data['target']
 
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
 
# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
 
# Make predictions and evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
 
print("Mean Squared Error:", mse)
