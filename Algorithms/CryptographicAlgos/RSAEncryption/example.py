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
