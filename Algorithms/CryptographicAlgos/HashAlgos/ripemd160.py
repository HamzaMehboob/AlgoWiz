import hashlib

def hash_ripemd160(input_string):
    ripemd160_hash = hashlib.new('ripemd160')
    ripemd160_hash.update(input_string.encode('utf-8'))
    return ripemd160_hash.hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"RIPEMD-160 hash: {hash_ripemd160(input_string)}")
