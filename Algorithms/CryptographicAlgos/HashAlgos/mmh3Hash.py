import mmh3

def hash_murmur(input_string):
    return mmh3.hash(input_string)

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"MurmurHash hash: {hash_murmur(input_string)}")
