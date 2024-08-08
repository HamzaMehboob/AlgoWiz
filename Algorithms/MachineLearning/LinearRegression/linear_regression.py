import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class LinearRegressor:
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X, y):
        """
        Fit the linear regression model using the provided data.
        
        :param X: Features (numpy array or pandas DataFrame)
        :param y: Target variable (numpy array or pandas Series)
        """
        self.model.fit(X, y)

    def predict(self, X):
        """
        Predict using the linear regression model.
        
        :param X: Features (numpy array or pandas DataFrame)
        :return: Predictions (numpy array)
        """
        return self.model.predict(X)

    def evaluate(self, X, y):
        """
        Evaluate the model using Mean Squared Error and R^2 score.
        
        :param X: Features (numpy array or pandas DataFrame)
        :param y: Target variable (numpy array or pandas Series)
        :return: (Mean Squared Error, R^2 score)
        """
        y_pred = self.predict(X)
        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        return mse, r2

    def plot(self, X, y):
        """
        Plot the linear regression result.
        
        :param X: Features (numpy array or pandas DataFrame)
        :param y: Target variable (numpy array or pandas Series)
        """
        plt.scatter(X, y, color='blue', label='Data Points')
        plt.plot(X, self.predict(X), color='red', linewidth=2, label='Regression Line')
        plt.xlabel('Feature')
        plt.ylabel('Target')
        plt.title('Linear Regression')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Example data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])

    # Create and train the model
    model = LinearRegressor()
    model.fit(X, y)

    # Predict and evaluate
    predictions = model.predict(X)
    mse, r2 = model.evaluate(X, y)
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    # Plot the results
    model.plot(X, y)
