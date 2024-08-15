from Crypto.Hash import MD4

def hash_md4(input_string):
    md4_hash = MD4.new()
    md4_hash.update(input_string.encode('utf-8'))
    return md4_hash.hexdigest()

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"MD4 hash: {hash_md4(input_string)}")
