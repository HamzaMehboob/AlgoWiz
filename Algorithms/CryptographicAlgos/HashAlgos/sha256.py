import hashlib

def hash_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"SHA-256 hash: {hash_sha256(input_string)}")
