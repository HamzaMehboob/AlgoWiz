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
