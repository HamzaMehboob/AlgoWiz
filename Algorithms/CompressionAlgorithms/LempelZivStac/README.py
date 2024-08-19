# Lempel-Ziv-Stac (LZ77 and LZ78) Algorithms

## Overview

Lempel-Ziv-Stac (LZ77 and LZ78) are foundational lossless data compression algorithms that work by finding and eliminating redundancy in data. These algorithms are the basis for many modern compression tools and formats, such as `gzip`, `PNG`, and more.

### LZ77

LZ77 works by sliding a window over the data to identify repeated sequences, which are then replaced with references to the previous occurrence of the sequence.

### LZ78

LZ78 builds a dictionary of substrings encountered in the data. New substrings are added to the dictionary as they are encountered, and subsequent occurrences are replaced by references to the dictionary.

## Example

### LZ77
- **Input:** `abracadabra`
- **Compressed:** `[(0, 0, 'a'), (0, 0, 'b'), (0, 0, 'r'), (3, 1, 'c'), (3, 2, 'd'), (7, 1, 'r')]`
- **Decompressed:** `abracadabra`

### LZ78
- **Input:** `abracadabra`
- **Compressed:** `[(0, 'a'), (0, 'b'), (0, 'r'), (1, 'c'), (4, 'd'), (1, 'r')]`
- **Decompressed:** `abracadabra`

## Files

- **lz77.py:** Contains the implementation of the LZ77 compression and decompression algorithms.
- **lz78.py:** Contains the implementation of the LZ78 compression and decompression algorithms.
- **example.py:** Demonstrates how to use the LZ77 and LZ78 algorithms with example data.

## Usage

### LZ77 Compression
```python
from lz77 import lz77_compress

data = "abracadabra"
compressed_data = lz77_compress(data)
print(f"Compressed Data: {compressed_data}")
