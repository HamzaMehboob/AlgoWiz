def lz77_compress(data, window_size=20):
    """Compress data using the LZ77 algorithm."""
    i = 0
    output = []

    while i < len(data):
        match = (-1, 0)
        for j in range(max(0, i - window_size), i):
            k = 0
            while i + k < len(data) and data[j + k] == data[i + k]:
                k += 1
            if k > match[1]:
                match = (i - j, k)

        if match[1] > 0:
            # Check if i + match[1] is within the bounds
            if i + match[1] < len(data):
                output.append((match[0], match[1], data[i + match[1]]))
            else:
                output.append((match[0], match[1], ''))
            i += match[1] + 1
        else:
            output.append((0, 0, data[i]))
            i += 1

    return output

def lz77_decompress(data):
    """Decompress data using the LZ77 algorithm."""
    output = []
    
    for offset, length, symbol in data:
        if offset == 0 and length == 0:
            output.append(symbol)
        else:
            start = len(output) - offset
            for i in range(length):
                output.append(output[start + i])
            if symbol:
                output.append(symbol)

    return ''.join(output)

# Example Usage
if __name__ == "__main__":
    original_text = "abracadabra"
    compressed = lz77_compress(original_text)
    print(f"Compressed: {compressed}")

    decompressed = lz77_decompress(compressed)
    print(f"Decompressed: {decompressed}")
