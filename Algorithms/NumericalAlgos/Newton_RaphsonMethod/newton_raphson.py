import numpy as np

class NewtonRaphson:
    def __init__(self, func, func_derivative, initial_guess, tolerance=1e-7, max_iterations=100):
        self.func = func
        self.func_derivative = func_derivative
        self.initial_guess = initial_guess
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def find_root(self):
        x = self.initial_guess
        for _ in range(self.max_iterations):
            fx = self.func(x)
            f_prime_x = self.func_derivative(x)

            if f_prime_x == 0:
                raise ValueError("Derivative is zero. No solution found.")

            x_new = x - fx / f_prime_x

            if abs(x_new - x) < self.tolerance:
                return x_new

            x = x_new

        raise ValueError("Maximum iterations exceeded. No solution found.")

# Example usage:
if __name__ == "__main__":
    def func(x):
        return x**3 - x - 2

    def func_derivative(x):
        return 3*x**2 - 1

    newton_raphson = NewtonRaphson(func, func_derivative, initial_guess=1.0)
    root = newton_raphson.find_root()
    print(f"The root of the function is approximately: {root}")
