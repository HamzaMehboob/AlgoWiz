import hashlib
import os

def hash_pbkdf2(password, salt=None, iterations=100000):
    salt = salt or os.urandom(16)
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations).hex()

if __name__ == "__main__":
    password = "mysecretpassword"
    print(f"PBKDF2 hash: {hash_pbkdf2(password)}")
