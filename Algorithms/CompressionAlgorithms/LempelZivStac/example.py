from lz77 import lz77_compress, lz77_decompress
from lz78 import lz78_compress, lz78_decompress

# Example text
original_text = "abracadabra"

# LZ77 Compression and Decompression
print("LZ77 Example:")
compressed_lz77 = lz77_compress(original_text)
print(f"Compressed LZ77: {compressed_lz77}")

decompressed_lz77 = lz77_decompress(compressed_lz77)
print(f"Decompressed LZ77: {decompressed_lz77}")

# Verify correctness
assert original_text == decompressed_lz77, "LZ77 transformation and inversion failed."
print("LZ77 transformation and inversion successful.\n")

# LZ78 Compression and Decompression
print("LZ78 Example:")
compressed_lz78 = lz78_compress(original_text)
print(f"Compressed LZ78: {compressed_lz78}")

decompressed_lz78 = lz78_decompress(compressed_lz78)
print(f"Decompressed LZ78: {decompressed_lz78}")

# Verify correctness
assert original_text == decompressed_lz78, "LZ78 transformation and inversion failed."
print("LZ78 transformation and inversion successful.")
