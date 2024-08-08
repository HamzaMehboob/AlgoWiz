from lzw_compression import LZW

def main():
    lzw = LZW()

    text = "TOBEORNOTTOBEORTOBEORNOT"
    print("Original text:", text)

    compressed_data = lzw.compress(text)
    print("Compressed data:", compressed_data)

    decompressed_data = lzw.decompress(compressed_data)
    print("Decompressed text:", decompressed_data)

if __name__ == "__main__":
    main()
