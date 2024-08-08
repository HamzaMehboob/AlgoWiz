# Newton-Raphson Method

The Newton-Raphson method is a numerical technique used to find approximations to the roots of a real-valued function.

## Features

- **Find Root**: Calculates the root of a given function using the Newton-Raphson iterative method.
- **Custom Function**: Allows for specifying a custom function and its derivative.

## Installation

This script requires `numpy`. Install it using pip:

```bash
pip install numpy


##Usage

1. Clone the repository or download the files.
2. Modify the func and func_derivative functions in example.py as needed.
3. Run the example.py script to see the Newton-Raphson method in action.


###EXAMPLE
Here is an example of how to use the Newton-Raphson method:
```python
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

    
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com