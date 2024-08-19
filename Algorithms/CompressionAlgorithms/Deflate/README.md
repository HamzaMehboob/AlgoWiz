# Deflate Compression Algorithm

## Overview

Deflate is a lossless data compression algorithm that combines LZ77 (dictionary-based compression) with Huffman coding (entropy coding) to achieve efficient compression. It is widely used in formats like PNG, ZIP, and GZIP.

## Files

- **deflate.py**: Contains the implementation of the Deflate compression and decompression algorithms, combining LZ77 and Huffman coding.
- **example.py**: Demonstrates how to use the Deflate algorithm with example data.
- **README.md**: Provides documentation for the Deflate algorithm.

## Usage

### Compressing Data

To compress text using the Deflate algorithm:

```python
from deflate import deflate_compress

original_text = "abracadabra"
compressed_data, huffman_codes = deflate_compress(original_text)
print(f"Compressed Data: {compressed_data}")
print(f"Huffman Codes: {huffman_codes}")
