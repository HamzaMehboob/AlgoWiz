import brotli

def brotli_compress(data):
    """Compress data using Brotli."""
    compressed = brotli.compress(data.encode('utf-8'))
    return compressed

def brotli_decompress(compressed_data):
    """Decompress data using Brotli."""
    decompressed = brotli.decompress(compressed_data).decode('utf-8')
    return decompressed

# Example Usage
if __name__ == "__main__":
    original_text = "abracadabra"
    
    compressed_data = brotli_compress(original_text)
    print(f"Compressed Data (binary): {compressed_data}")
    
    decompressed_data = brotli_decompress(compressed_data)
    print(f"Decompressed Data: {decompressed_data}")
    
    # Verify correctness
    assert original_text == decompressed_data, "Brotli compression and decompression failed."
    print("Brotli compression and decompression successful.")
