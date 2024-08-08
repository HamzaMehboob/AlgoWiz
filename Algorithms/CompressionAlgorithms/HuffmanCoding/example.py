from huffman_coding import huffman_encoding, huffman_decoding

def main():
    text = "this is an example for huffman encoding"
    print("Original text:", text)

    encoded_text, huffman_codes = huffman_encoding(text)
    print("Encoded text:", encoded_text)
    print("Huffman Codes:", huffman_codes)

    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print("Decoded text:", decoded_text)

if __name__ == "__main__":
    main()
