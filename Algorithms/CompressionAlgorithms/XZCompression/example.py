from xz_compression import xz_compress, xz_decompress

# Example text
original_text = "abracadabra"

# Compress the text
compressed_data = xz_compress(original_text)
print(f"Original Text: {original_text}")
print(f"Compressed Data (binary): {compressed_data}")

# Decompress the text
decompressed_data = xz_decompress(compressed_data)
print(f"Decompressed Data: {decompressed_data}")

# Verify correctness
assert original_text == decompressed_data, "XZ compression and decompression failed."
print("XZ compression and decompression successful.")
