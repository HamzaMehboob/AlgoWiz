from Crypto.Util.number import getPrime, GCD
import random

class DiffieHellman:
    def __init__(self, key_size=2048):
        self.p = getPrime(key_size)
        self.g = random.randint(2, self.p - 2)
        self.private_key = random.randint(2, self.p - 2)
        self.public_key = pow(self.g, self.private_key, self.p)

    def generate_shared_key(self, other_public_key):
        shared_key = pow(other_public_key, self.private_key, self.p)
        return shared_key

    def get_public_key(self):
        return self.public_key

    def get_params(self):
        return (self.p, self.g)
