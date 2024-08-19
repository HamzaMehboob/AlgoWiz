from ppm import ppm_train, ppm_compress, ppm_decompress

# Example text
original_text = "abracadabra"
order = 3

# Train PPM model
model = ppm_train(original_text, order)

# Compress the text
compressed_data = ppm_compress(original_text, order, model)
print(f"Original Text: {original_text}")
print(f"Compressed Data: {compressed_data}")

# Decompress the text
decompressed_data = ppm_decompress(compressed_data, order, model)
print(f"Decompressed Data: {decompressed_data}")

# Verify correctness
assert original_text[:len(decompressed_data)] == decompressed_data, "PPM compression and decompression failed."
print("PPM compression and decompression successful.")
