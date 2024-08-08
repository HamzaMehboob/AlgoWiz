import numpy as np
from linear_regression import LinearRegressor

def main():
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

if __name__ == "__main__":
    main()
