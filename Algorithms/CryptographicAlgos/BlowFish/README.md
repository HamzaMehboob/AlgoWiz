# Blowfish Cryptographic Algorithm

## Overview

Blowfish is a symmetric-key block cipher designed in 1993 by Bruce Schneier. It is known for its simplicity and effectiveness, with a variable-length key ranging from 32 bits to 448 bits. Blowfish is widely used in various cryptographic applications due to its speed and security.

## Structure

This implementation is divided into the following files:

- **blowfish.py**: Contains the Blowfish class implementation, including key expansion, encryption, and decryption methods.
- **example.py**: Demonstrates how to use the Blowfish class to encrypt and decrypt data.
- **README.md**: Provides an overview of the project and usage instructions.

## Usage

### Initialization

To use Blowfish, first, initialize the Blowfish object with a key:

```python
from blowfish import Blowfish

key = b"your_secret_key"
bf = Blowfish(key)
