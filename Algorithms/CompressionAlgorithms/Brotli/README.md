# Brotli Compression

## Overview

Brotli is a compression algorithm developed by Google that offers a high compression ratio and efficient performance. It is widely used for web compression (e.g., HTTP compression) and provides a balance between speed and compression ratio.

## Files

- **brotli_compression.py**: Contains the implementation of Brotli compression and decompression using the `brotli` Python library.
- **example.py**: Demonstrates how to use the Brotli compression functions.
- **README.md**: Provides documentation for Brotli compression.

## Brotli Compression

### `brotli_compress(data)`

Compresses the input `data` using Brotli. The data is expected to be a string, and it will be encoded into bytes before compression.

### `brotli_decompress(compressed_data)`

Decompresses the `compressed_data` using Brotli. The data is expected to be in bytes format and will be decoded back into a string after decompression.

## Usage

### Compressing Data

To compress text using Brotli:

```python
from brotli_compression import brotli_compress

original_text = "abracadabra"
compressed_data = brotli_compress(original_text)
print(f"Compressed Data (binary): {compressed_data}")
