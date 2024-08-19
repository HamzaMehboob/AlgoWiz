# Burrows-Wheeler Transform (BWT) Algorithm

## Overview

The Burrows-Wheeler Transform (BWT) is a block-sorting data compression algorithm that reorganizes a string of characters into runs of similar characters. This makes the data more amenable to compression algorithms like Run-Length Encoding (RLE) or Huffman coding.

BWT is widely used in data compression tools like bzip2.

### Example
- **Input:** `banana`
- **BWT Output:** `annb$aa` (example transformed string) and its index
- **Inverse BWT:** Reconstructs the original string from the BWT output.

## Files

- **bwt.py:** Contains the implementation of the Burrows-Wheeler Transform and its inverse.
- **example.py:** Demonstrates how to use the BWT algorithm with example data.

## Usage

### Applying BWT
```python
from bwt import bwt_transform

data = "banana"
transformed, index = bwt_transform(data)
print(f"Transformed: {transformed}, Index: {index}")
