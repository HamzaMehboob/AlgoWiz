import hashlib

def hash_sha3_256(input_string):
    sha3_256_hash = hashlib.sha3_256()
    sha3_256_hash.update(input_string.encode('utf-8'))
    return sha3_256_hash.hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"SHA-3-256 hash: {hash_sha3_256(input_string)}")
