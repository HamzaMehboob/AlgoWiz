# Arithmetic Coding Algorithm

## Overview

Arithmetic Coding is a sophisticated form of entropy encoding used in lossless data compression. Unlike traditional methods that encode each symbol separately, Arithmetic Coding represents the entire message as a single number within the interval [0,1).

### Example
- **Input:** `hello_world`
- **Encoded:** `0.596329` (example encoded value)
- **Decoded:** `hello_world`

## Files

- **arithmetic_coding.py:** Contains the implementation of the Arithmetic Coding compression and decompression algorithms.
- **example.py:** Demonstrates how to use the Arithmetic Coding algorithm with example data.

## Usage

### Encoding
```python
from arithmetic_coding import arithmetic_encode, build_probability_table

data = "hello_world"
prob_table = build_probability_table(data)
encoded_value = arithmetic_encode(data, prob_table)
print(f"Encoded: {encoded_value}")