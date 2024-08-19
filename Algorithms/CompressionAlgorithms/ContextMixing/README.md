# Context Mixing Compression

## Overview

Context Mixing is a technique used in data compression that blends multiple prediction models to improve the accuracy of predictions. It is often used in advanced compression algorithms such as Prediction by Partial Matching (PPM).

## Files

- **context_mixing.py**: Contains the implementation of Context Mixing for compression and decompression.
- **example.py**: Demonstrates how to use the Context Mixing functions.
- **README.md**: Provides documentation for Context Mixing compression.

## Context Mixing Compression

### `ContextMixingCompressor`

#### `__init__(self, order=2)`

Initializes the ContextMixingCompressor with a given order. The order defines the length of the context used for prediction.

#### `compress(self, data)`

Compresses the input `data` using Context Mixing. The data is expected to be a string, and it will be encoded into bytes before compression.

#### `decompress(self, compressed_data)`

Decompresses the `compressed_data` using Context Mixing. The data is expected to be a list of integers (compressed data) and will be decoded back into a string after decompression.

## Usage

### Compressing Data

To compress text using Context Mixing:

```python
from context_mixing import ContextMixingCompressor

compressor = ContextMixingCompressor(order=2)
compressed_data = compressor.compress("abracadabra")
print(f"Compressed Data: {compressed_data}")
