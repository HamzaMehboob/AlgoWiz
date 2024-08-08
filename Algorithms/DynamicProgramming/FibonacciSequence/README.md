# Fibonacci Sequence Generator

This repository contains an implementation of a Fibonacci Sequence generator in Python. The Fibonacci Sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

## Introduction

The Fibonacci Sequence is commonly used in programming exercises and mathematical problems. This implementation provides a simple way to generate the first `n` numbers in the sequence.

## Features

- Generates the first `n` numbers in the Fibonacci Sequence.
- Provides a clear and easy-to-use class-based implementation.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/DynamicProgramming/FibonacciSequence
    ```

2. Run the example script:
    ```sh
    python example.py
    ```

## Example

Here is an example usage of the Fibonacci Sequence generator:

```python
from fibonacci import Fibonacci

n = 15  # Number of Fibonacci numbers to generate
fib = Fibonacci(n)

print(f"First {n} Fibonacci numbers: {fib.generate()}")

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com