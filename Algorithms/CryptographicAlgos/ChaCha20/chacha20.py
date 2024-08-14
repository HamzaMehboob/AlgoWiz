from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import base64

class ChaCha20Cipher:
    def __init__(self, key=None):
        self.key = key or get_random_bytes(32)

    def encrypt(self, plaintext):
        cipher = ChaCha20.new(key=self.key)
        ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
        return base64.b64encode(cipher.nonce + ciphertext).decode('utf-8')

    def decrypt(self, encrypted_text):
        data = base64.b64decode(encrypted_text.encode('utf-8'))
        nonce = data[:8]
        ciphertext = data[8:]
        cipher = ChaCha20.new(key=self.key, nonce=nonce)
        return cipher.decrypt(ciphertext).decode('utf-8')
