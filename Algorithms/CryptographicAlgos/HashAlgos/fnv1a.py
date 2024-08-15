def fnv1a_hash(input_string):
    fnv_prime = 0x1000193
    hash_value = 0x811c9dc5
    
    for char in input_string:
        hash_value ^= ord(char)
        hash_value *= fnv_prime
    
    return format(hash_value & 0xffffffff, '08x')

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"FNV-1a hash: {fnv1a_hash(input_string)}")
