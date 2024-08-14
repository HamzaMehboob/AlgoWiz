# Elliptic Curve Cryptography (ECC)

This project implements the Elliptic Curve Cryptography (ECC) algorithm in Python using the `pycryptodome` library. ECC is a public key cryptography system that offers strong security with smaller keys compared to traditional algorithms like RSA.

## Files
- **`ecc.py`**: Contains the `ECCCrypto` class, which provides methods for key generation, signing, and verification.
- **`example.py`**: Demonstrates how to use the `ECCCrypto` class.
- **`README.md`**: Documentation for the project.

Usage
To use the ECC algorithm, you can run the example.py script:


```bash
python example.py
This script will:

Generate an ECC key pair.
Sign a message using the private key.
Verify the signature using the public key.