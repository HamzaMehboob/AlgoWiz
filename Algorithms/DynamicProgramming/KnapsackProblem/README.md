# Knapsack Problem Algorithm

This repository contains an implementation of the 0/1 Knapsack Problem algorithm in Python. The Knapsack Problem is a classic optimization problem used to determine the maximum value of items that can be carried in a knapsack of limited capacity.

## Introduction

The 0/1 Knapsack Problem involves a knapsack with a maximum weight capacity and a set of items, each with a specific weight and value. The goal is to determine the maximum value that can be obtained by selecting a subset of items such that their total weight does not exceed the knapsack's capacity.

## Features

- Solves the 0/1 Knapsack Problem using dynamic programming.
- Calculates the maximum value that can be obtained.
- Identifies the indices of the selected items.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/DynamicProgramming/KnapsackProblem
    ```

2. Run the example script:
    ```sh
    python example.py
    ```

## Example

Here is an example usage of the Knapsack algorithm:

```python
from knapsack import Knapsack

capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]

knapsack = Knapsack(capacity, weights, values)

print("Maximum value in Knapsack:", knapsack.solve())
print("Selected item indices:", knapsack.get_selected_items())

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com