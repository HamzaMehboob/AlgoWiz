from newton_raphson import NewtonRaphson

def main():
    # Define the function and its derivative
    def func(x):
        return x**3 - x - 2

    def func_derivative(x):
        return 3*x**2 - 1

    # Create a NewtonRaphson object
    newton_raphson = NewtonRaphson(func, func_derivative, initial_guess=1.0)

    # Find the root
    try:
        root = newton_raphson.find_root()
        print(f"The root of the function is approximately: {root}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
