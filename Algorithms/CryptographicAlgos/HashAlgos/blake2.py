import hashlib

def hash_blake2b(input_string):
    blake2b_hash = hashlib.blake2b()
    blake2b_hash.update(input_string.encode('utf-8'))
    return blake2b_hash.hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"Blake2b hash: {hash_blake2b(input_string)}")
