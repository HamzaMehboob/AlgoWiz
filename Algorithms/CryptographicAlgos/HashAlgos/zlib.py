import zlib

def hash_crc32(input_string):
    return format(zlib.crc32(input_string.encode('utf-8')), '08x')

if __name__ == "__main__":
    input_string = "Hello, world!"
    print(f"CRC32 hash: {hash_crc32(input_string)}")
