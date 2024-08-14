from chacha20 import ChaCha20Cipher

# Initialize ChaCha20 with a random key
cipher = ChaCha20Cipher()

# Message to be encrypted
plaintext = "This is a secret message."

# Encrypt the message
encrypted_text = cipher.encrypt(plaintext)
print(f"Encrypted: {encrypted_text}")

# Decrypt the message
decrypted_text = cipher.decrypt(encrypted_text)
print(f"Decrypted: {decrypted_text}")
