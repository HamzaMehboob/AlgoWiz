# Zstandard (Zstd) Compression

## Overview

Zstandard (Zstd) is a fast compression algorithm developed by Facebook. It provides a good balance between compression ratio and speed, making it suitable for a variety of applications.

## Files

- **zstd_compression.py**: Contains the implementation of Zstandard compression and decompression using the `zstandard` Python library.
- **requirements.txt**: Contains the pip install requirements for the ZStandard.
- **example.py**: Demonstrates how to use the Zstandard compression functions.
- **README.md**: Provides documentation for Zstandard compression.

## Zstandard Compression

### `zstd_compress(data)`

Compresses the input `data` using Zstandard. The data is expected to be a string, and it will be encoded into bytes before compression.

### `zstd_decompress(compressed_data)`

Decompresses the `compressed_data` using Zstandard. The data is expected to be in bytes format and will be decoded back into a string after decompression.

## Usage

### Compressing Data

To compress text using Zstandard:

```python
from zstd_compression import zstd_compress

original_text = "abracadabra"
compressed_data = zstd_compress(original_text)
print(f"Compressed Data (binary): {compressed_data}")
