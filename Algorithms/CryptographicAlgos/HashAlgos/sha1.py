import hashlib

def hash_sha1(input_string):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_string.encode('utf-8'))
    return sha1_hash.hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"SHA-1 hash: {hash_sha1(input_string)}")
