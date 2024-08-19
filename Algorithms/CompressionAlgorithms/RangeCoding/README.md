# Range Coding Algorithm

## Overview

Range Coding is an entropy encoding method similar to Arithmetic Coding. It compresses data by representing sequences of symbols as a single value within an interval [0,1). Range Coding is efficient and effective for high-precision data compression tasks, making it a popular choice in various applications that require lossless compression.

### Example
- **Input:** `hello_world`
- **Encoded Value:** A floating-point number representing the compressed sequence.
- **Decoded Output:** Reconstructs the original string from the encoded value.

## Files

- **range_coding.py:** Contains the implementation of the Range Coding compression and decompression algorithms.
- **example.py:** Demonstrates how to use the Range Coding algorithm with example data.

## Usage

### Building the Probability Table

To encode data using Range Coding, you first need to build a cumulative probability table based on the frequency of each symbol in the data:

```python
from range_coding import build_probability_table

data = "hello_world"
prob_table = build_probability_table(data)
print(f"Probability Table: {prob_table}")
