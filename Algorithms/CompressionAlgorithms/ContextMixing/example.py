from context_mixing import ContextMixingCompressor

# Example text
original_text = "abracadabra"

# Create a ContextMixingCompressor instance
compressor = ContextMixingCompressor(order=2)

# Compress the text
compressed_data = compressor.compress(original_text)
print(f"Original Text: {original_text}")
print(f"Compressed Data: {compressed_data}")

# Decompress the text
decompressed_data = compressor.decompress(compressed_data)
print(f"Decompressed Data: {decompressed_data}")

# Verify correctness
assert original_text == decompressed_data, "Context Mixing compression and decompression failed."
print("Context Mixing compression and decompression successful.")
