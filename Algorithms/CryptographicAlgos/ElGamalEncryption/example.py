from ElGamal import ElGamal

if __name__ == "__main__":
    elgamal = ElGamal()
    plaintext = "Hello, ElGamal!"
    ciphertext = elgamal.encrypt(plaintext)
    print("Ciphertext:", ciphertext)
    decrypted_text = elgamal.decrypt(ciphertext)
    print("Decrypted text:", decrypted_text)
