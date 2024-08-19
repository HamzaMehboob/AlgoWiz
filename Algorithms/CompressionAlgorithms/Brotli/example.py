from brotli_compression import brotli_compress, brotli_decompress

# Example text
original_text = "abracadabra"

# Compress the text
compressed_data = brotli_compress(original_text)
print(f"Original Text: {original_text}")
print(f"Compressed Data (binary): {compressed_data}")

# Decompress the text
decompressed_data = brotli_decompress(compressed_data)
print(f"Decompressed Data: {decompressed_data}")

# Verify correctness
assert original_text == decompressed_data, "Brotli compression and decompression failed."
print("Brotli compression and decompression successful.")
