from rle import rle_encode, rle_decode

# Example Usage
if __name__ == "__main__":
    original_text = "AAAABBBCCDAA"
    encoded_data = rle_encode(original_text)
    print(f"Encoded: {encoded_data}")
    decoded_data = rle_decode(encoded_data)
    print(f"Decoded: {decoded_data}")