# AES Encryption

AES (Advanced Encryption Standard) is a symmetric encryption algorithm used to encrypt data. This repository provides a Python implementation of AES encryption and decryption.

## Features

- **Encryption**: Encrypt messages using AES.
- **Decryption**: Decrypt messages using AES.
- **Key Generation**: Generate a random AES key.

## Installation

You need to install the `pycryptodome` library for AES encryption. Install it using pip:

```bash
pip install pycryptodome

##Usage

1. Clone the repository or download the files.
2. Run the example.py script to see AES encryption and decryption in action.

###EXAMPLE
from aes_encryption import AESEncryption

def main():
    aes = AESEncryption()

    # Get the key
    key = aes.get_key()
    print("AES Key:")
    print(key)

    # Encrypt and Decrypt a message
    message = "Hello, AES Encryption!"
    print("\nOriginal Message:", message)

    encrypted_message = aes.encrypt(message)
    print("\nEncrypted Message:", encrypted_message)

    decrypted_message = aes.decrypt(encrypted_message)
    print("\nDecrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com