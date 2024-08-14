from tripledes import TripleDES

if __name__ == "__main__":
    key = "your_secret_key"
    data = "Sensitive data that needs encryption"

    tdes = TripleDES(key)

    # Encryption
    encrypted_data = tdes.encrypt(data.encode('utf-8'))
    print(f"Encrypted Data: {encrypted_data}")

    # Decryption
    decrypted_data = tdes.decrypt(encrypted_data)
    print(f"Decrypted Data: {decrypted_data.decode('utf-8')}")
