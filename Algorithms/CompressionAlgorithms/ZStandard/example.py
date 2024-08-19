from zstd_compression import zstd_compress, zstd_decompress

# Example text
original_text = "abracadabra"

# Compress the text
compressed_data = zstd_compress(original_text)
print(f"Original Text: {original_text}")
print(f"Compressed Data (binary): {compressed_data}")

# Decompress the text
decompressed_data = zstd_decompress(compressed_data)
print(f"Decompressed Data: {decompressed_data}")

# Verify correctness
assert original_text == decompressed_data, "Zstandard compression and decompression failed."
print("Zstandard compression and decompression successful.")
