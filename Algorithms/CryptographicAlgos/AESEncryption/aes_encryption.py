from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib

class AESEncryption:
    def __init__(self):
        # Generate a random 256-bit key
        self.key = get_random_bytes(32)
        self.cipher = AES.new(self.key, AES.MODE_EAX)

    def encrypt(self, message):
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(message.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt(self, encrypted_message):
        data = base64.b64decode(encrypted_message)
        nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_message.decode()

    def get_key(self):
        return base64.b64encode(self.key).decode()
