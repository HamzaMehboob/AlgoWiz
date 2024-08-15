from blake3 import blake3

def hash_blake3(input_string):
    return blake3(input_string.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"BLAKE3 hash: {hash_blake3(input_string)}")
