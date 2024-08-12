from Crypto.Util.number import getPrime, GCD, inverse, bytes_to_long, long_to_bytes
import random

class ElGamal:
    def __init__(self, key_size=1024):
        self.p = getPrime(key_size)
        self.g = random.randint(2, self.p - 2)
        self.x = random.randint(1, self.p - 2)
        self.h = pow(self.g, self.x, self.p)

    def encrypt(self, plaintext):
        y = random.randint(1, self.p - 2)
        c1 = pow(self.g, y, self.p)
        s = pow(self.h, y, self.p)
        c2 = (bytes_to_long(plaintext.encode('utf-8')) * s) % self.p
        return (c1, c2)

    def decrypt(self, ciphertext):
        c1, c2 = ciphertext
        s = pow(c1, self.x, self.p)
        plaintext = (c2 * inverse(s, self.p)) % self.p
        return long_to_bytes(plaintext).decode('utf-8')