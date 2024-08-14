# Triple DES (3DES) Encryption

This project implements the Triple DES (3DES) encryption algorithm in Python using the `pycryptodome` library. Triple DES is an enhancement of the Data Encryption Standard (DES) that applies the DES algorithm three times to each data block for increased security.

## Files
- **`tripledes.py`**: Contains the `TripleDES` class, which provides methods for encryption and decryption.
- **`example.py`**: Demonstrates how to use the `TripleDES` class.
- **`README.md`**: Documentation for the project.
- **`requirements.txt`**: Lists the dependencies needed for the project.

## Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt


## Usage
To use the Triple DES algorithm, you can run the example.py script:

```bash
python example.py

This script will:

Encrypt a given plaintext using a secret key.
Decrypt the encrypted data back to its original plaintext.