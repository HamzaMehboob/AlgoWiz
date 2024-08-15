import hashlib

def hash_sha512(input_string):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(input_string.encode('utf-8'))
    return sha512_hash.hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"SHA-512 hash: {hash_sha512(input_string)}")
