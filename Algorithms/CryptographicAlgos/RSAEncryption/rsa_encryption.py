from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

class RSAEncryption:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()
        self.cipher = PKCS1_OAEP.new(self.public_key)

    def encrypt(self, message):
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_message = cipher.encrypt(message.encode())
        return base64.b64encode(encrypted_message).decode()

    def decrypt(self, encrypted_message):
        encrypted_message = base64.b64decode(encrypted_message)
        cipher = PKCS1_OAEP.new(self.key)
        decrypted_message = cipher.decrypt(encrypted_message)
        return decrypted_message.decode()

    def get_keys(self):
        return {
            'private_key': self.key.export_key().decode(),
            'public_key': self.public_key.export_key().decode()
        }
