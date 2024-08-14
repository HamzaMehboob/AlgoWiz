from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import hashlib

class TripleDES:
    def __init__(self, key):
        self.key = self.prepare_key(key)
        self.cipher = DES3.new(self.key, DES3.MODE_ECB)

    def prepare_key(self, key):
        hasher = hashlib.sha256()
        hasher.update(key.encode('utf-8'))
        return hasher.digest()[:24]

    def encrypt(self, plaintext):
        plaintext_padded = self.pad(plaintext)
        return self.cipher.encrypt(plaintext_padded)

    def decrypt(self, ciphertext):
        decrypted_data = self.cipher.decrypt(ciphertext)
        return self.unpad(decrypted_data)

    def pad(self, data):
        pad_len = 8 - len(data) % 8
        return data + bytes([pad_len] * pad_len)

    def unpad(self, data):
        pad_len = data[-1]
        return data[:-pad_len]
