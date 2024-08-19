import lzma

def xz_compress(data):
    """Compress data using XZ (LZMA)."""
    compressed = lzma.compress(data.encode('utf-8'))
    return compressed

def xz_decompress(compressed_data):
    """Decompress data using XZ (LZMA)."""
    decompressed = lzma.decompress(compressed_data).decode('utf-8')
    return decompressed

# Example Usage
if __name__ == "__main__":
    original_text = "abracadabra"
    
    compressed_data = xz_compress(original_text)
    print(f"Compressed Data (binary): {compressed_data}")
    
    decompressed_data = xz_decompress(compressed_data)
    print(f"Decompressed Data: {decompressed_data}")
    
    # Verify correctness
    assert original_text == decompressed_data, "XZ compression and decompression failed."
    print("XZ compression and decompression successful.")
