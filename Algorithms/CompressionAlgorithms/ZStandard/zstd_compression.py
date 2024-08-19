import zstandard as zstd

def zstd_compress(data):
    """Compress data using Zstandard."""
    cctx = zstd.ZstdCompressor()
    compressed = cctx.compress(data.encode('utf-8'))
    return compressed

def zstd_decompress(compressed_data):
    """Decompress data using Zstandard."""
    dctx = zstd.ZstdDecompressor()
    decompressed = dctx.decompress(compressed_data).decode('utf-8')
    return decompressed

# Example Usage
if __name__ == "__main__":
    original_text = "abracadabra"
    
    compressed_data = zstd_compress(original_text)
    print(f"Compressed Data (binary): {compressed_data}")
    
    decompressed_data = zstd_decompress(compressed_data)
    print(f"Decompressed Data: {decompressed_data}")
    
    # Verify correctness
    assert original_text == decompressed_data, "Zstandard compression and decompression failed."
    print("Zstandard compression and decompression successful.")
