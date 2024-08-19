# Run-Length Encoding (RLE) Algorithm

## Overview

Run-Length Encoding (RLE) is a simple lossless data compression algorithm that compresses data by identifying sequences of repeating characters and encoding them as a single character followed by the number of repetitions.

### Example
- **Input:** `AAAABBBCCDAA`
- **Encoded:** `A4B3C2D1A2`
- **Decoded:** `AAAABBBCCDAA`

## Files

- **rle.py:** Contains the implementation of the RLE compression and decompression algorithms.
- **example.py:** Demonstrates how to use the RLE algorithm with example data.

## Usage

### Encoding
```python
from rle import rle_encode

data = "AAAABBBCCDAA"
encoded = rle_encode(data)
print(f"Encoded: {encoded}")
