import xxhash

def hash_xxhash(input_string):
    return xxhash.xxh32(input_string).hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"XXHash hash: {hash_xxhash(input_string)}")
