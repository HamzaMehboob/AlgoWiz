# Huffman Coding

Huffman coding is a popular method of lossless data compression. This repository provides a Python implementation of the Huffman Coding algorithm.

## Features

- **Encoding**: Convert text to Huffman encoded binary string.
- **Decoding**: Convert Huffman encoded binary string back to original text.

## Installation

No additional libraries are required. This implementation uses only Python's built-in features.

## Usage

1. Clone the repository or download the files.
2. Run the `example.py` script to see Huffman Coding in action.

### Example

```python
from huffman_coding import huffman_encoding, huffman_decoding

def main():
    text = "this is an example for huffman encoding"
    print("Original text:", text)

    encoded_text, huffman_codes = huffman_encoding(text)
    print("Encoded text:", encoded_text)
    print("Huffman Codes:", huffman_codes)

    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print("Decoded text:", decoded_text)

if __name__ == "__main__":
    main()

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com