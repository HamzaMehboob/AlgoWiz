# XZ (LZMA) Compression

## Overview

XZ (LZMA) is a high-compression ratio algorithm that is known for its efficiency in compressing data with high compression ratios. It is commonly used in file formats such as `.xz` and `.lzma`.

## Files

- **xz_compression.py**: Contains the implementation of XZ (LZMA) compression and decompression using Python's `lzma` library.
- **example.py**: Demonstrates how to use the XZ compression functions.
- **README.md**: Provides documentation for XZ compression.

## XZ Compression

### `xz_compress(data)`

Compresses the input `data` using XZ (LZMA). The data is expected to be a string, and it will be encoded into bytes before compression.

### `xz_decompress(compressed_data)`

Decompresses the `compressed_data` using XZ (LZMA). The data is expected to be in bytes format and will be decoded back into a string after decompression.

## Usage

### Compressing Data

To compress text using XZ (LZMA):

```python
from xz_compression import xz_compress

original_text = "abracadabra"
compressed_data = xz_compress(original_text)
print(f"Compressed Data (binary): {compressed_data}")
