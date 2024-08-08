# LZW Compression

LZW (Lempel-Ziv-Welch) is a lossless data compression algorithm. This repository provides a Python implementation of the LZW compression and decompression algorithms.

## Features

- **Compression**: Convert text to LZW compressed data.
- **Decompression**: Convert LZW compressed data back to original text.

## Installation

No additional libraries are required. This implementation uses only Python's built-in features.

## Usage

1. Clone the repository or download the files.
2. Run the `example.py` script to see LZW Compression in action.

### Example

```python
from lzw_compression import LZW

def main():
    lzw = LZW()

    text = "TOBEORNOTTOBEORTOBEORNOT"
    print("Original text:", text)

    compressed_data = lzw.compress(text)
    print("Compressed data:", compressed_data)

    decompressed_data = lzw.decompress(compressed_data)
    print("Decompressed text:", decompressed_data)

if __name__ == "__main__":
    main()

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com