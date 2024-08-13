from blowfish import Blowfish

def main():
    key = b'mysecurekey'
    bf = Blowfish(key)

    plaintext = b'example!'
    encrypted = bf.encrypt(plaintext)
    print(f"Encrypted data: {encrypted}")

    decrypted = bf.decrypt(encrypted)
    print(f"Decrypted data: {decrypted}")

if __name__ == "__main__":
    main()
