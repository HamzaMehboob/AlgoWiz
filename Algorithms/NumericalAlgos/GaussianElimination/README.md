# Gaussian Elimination

Gaussian Elimination is a numerical method for solving systems of linear equations. This repository provides a Python implementation of the Gaussian Elimination algorithm.

## Features

- **Forward Elimination**: Converts the matrix to upper triangular form.
- **Back Substitution**: Solves the upper triangular system to find the solution.

## Installation

No additional packages are required beyond Python's standard library, but `numpy` is used for matrix operations. Install it using pip:

```bash
pip install numpy


##Usage


1. Clone the repository or download the files.
2. Run the example.py script to see Gaussian Elimination in action.


###Example
```python
from gaussian_elimination import GaussianElimination

def main():
    # Example matrix and right-hand side vector
    matrix = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    gaussian = GaussianElimination(matrix, b)
    solution = gaussian.solve()

    print("Matrix A:")
    for row in matrix:
        print(row)

    print("\nRight-hand side vector b:")
    print(b)

    print("\nSolution vector x:")
    print(solution)

if __name__ == "__main__":
    main()

    
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com