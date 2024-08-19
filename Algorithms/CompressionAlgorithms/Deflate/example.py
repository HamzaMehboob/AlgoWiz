from deflate import deflate_compress, deflate_decompress

# Example text
original_text = "abracadabra"

# Compress the text
compressed_data, huffman_codes = deflate_compress(original_text)
print(f"Original Text: {original_text}")
print(f"Compressed Data: {compressed_data}")
print(f"Huffman Codes: {huffman_codes}")

# Decompress the text
decompressed_data = deflate_decompress(compressed_data, huffman_codes)
print(f"Decompressed Data: {decompressed_data}")

# Verify correctness
assert original_text == decompressed_data, "Deflate compression and decompression failed."
print("Deflate compression and decompression successful.")
