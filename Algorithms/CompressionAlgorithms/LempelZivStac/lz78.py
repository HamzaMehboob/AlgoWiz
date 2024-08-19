def lz78_compress(data):
    """Compress data using the LZ78 algorithm."""
    dictionary = {}
    i = 0
    output = []
    w = ""

    while i < len(data):
        w += data[i]
        if w not in dictionary:
            dictionary[w] = len(dictionary) + 1
            if len(w) > 1:
                output.append((dictionary[w[:-1]], w[-1]))
            else:
                output.append((0, w[-1]))
            w = ""
        i += 1

    if w:
        output.append((dictionary[w[:-1]], w[-1]))

    return output

def lz78_decompress(data):
    """Decompress data using the LZ78 algorithm."""
    dictionary = {0: ""}
    output = []
    
    for index, symbol in data:
        entry = dictionary[index] + symbol
        output.append(entry)
        dictionary[len(dictionary)] = entry

    return ''.join(output)

# Example Usage
if __name__ == "__main__":
    original_text = "abracadabra"
    compressed = lz78_compress(original_text)
    print(f"Compressed: {compressed}")

    decompressed = lz78_decompress(compressed)
    print(f"Decompressed: {decompressed}")
