# RSA Encryption

RSA is a public-key cryptosystem that is widely used for secure data transmission. This repository provides a Python implementation of RSA encryption and decryption.

## Features

- **Encryption**: Encrypt messages using RSA public key.
- **Decryption**: Decrypt messages using RSA private key.
- **Key Generation**: Generate RSA public and private keys.

## Installation

You need to install the `pycryptodome` library for RSA encryption. Install it using pip:

```bash
pip install pycryptodome

## Usage

1. Clone the repository or download the files.
2. Run the example.py script to see RSA encryption and decryption in action.


###EXAMPLE
from rsa_encryption import RSAEncryption

def main():
    rsa = RSAEncryption()

    # Get public and private keys
    keys = rsa.get_keys()
    print("Public Key:")
    print(keys['public_key'])
    print("\nPrivate Key:")
    print(keys['private_key'])

    # Encrypt and Decrypt a message
    message = "Hello, RSA Encryption!"
    print("\nOriginal Message:", message)

    encrypted_message = rsa.encrypt(message)
    print("\nEncrypted Message:", encrypted_message)

    decrypted_message = rsa.decrypt(encrypted_message)
    print("\nDecrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com