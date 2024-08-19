def rle_encode(data):
    """Run-Length Encoding (RLE) compression."""
    encoding = []
    i = 0

    while i < len(data):
        count = 1

        # Count occurrences of the same character
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1

        # Store the character and its count
        encoding.append((data[i], count))
        i += 1

    return encoding

def rle_decode(data):
    """Run-Length Encoding (RLE) decompression."""
    decoded = []

    for char, count in data:
        decoded.append(char * count)

    return ''.join(decoded)


