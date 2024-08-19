from collections import defaultdict
import heapq
import itertools

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_huffman_codes(root, prefix='', codebook=defaultdict()):
    if root is not None:
        if root.char is not None:
            codebook[root.char] = prefix
        build_huffman_codes(root.left, prefix + '0', codebook)
        build_huffman_codes(root.right, prefix + '1', codebook)
    return codebook

def huffman_compress(data):
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1
    
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = build_huffman_codes(huffman_tree)
    
    compressed_data = ''.join(huffman_codes[char] for char in data)
    return compressed_data, huffman_codes

def huffman_decompress(compressed_data, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ''
    decoded_data = []
    
    for bit in compressed_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ''
    
    return ''.join(decoded_data)

def lz77_compress(data, window_size=20):
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

def deflate_compress(data, lz77_window_size=20):
    lz77_compressed = lz77_compress(data, lz77_window_size)
    lz77_string = ''.join(f"{offset:02x}{length:02x}{symbol}" for offset, length, symbol in lz77_compressed)
    
    compressed_data, huffman_codes = huffman_compress(lz77_string)
    return compressed_data, huffman_codes

def deflate_decompress(compressed_data, huffman_codes, lz77_window_size=20):
    lz77_string = huffman_decompress(compressed_data, huffman_codes)
    lz77_compressed = [(int(lz77_string[i:i+2], 16), int(lz77_string[i+2:i+4], 16), lz77_string[i+4:i+5]) for i in range(0, len(lz77_string), 5)]
    
    return lz77_decompress(lz77_compressed)

# Example Usage
if __name__ == "__main__":
    original_text = "abracadabra"
    
    compressed, huffman_codes = deflate_compress(original_text)
    print(f"Compressed Data: {compressed}")
    print(f"Huffman Codes: {huffman_codes}")
    
    decompressed = deflate_decompress(compressed, huffman_codes)
    print(f"Decompressed Data: {decompressed}")
    
    assert original_text == decompressed, "Deflate compression and decompression failed."
    print("Deflate compression and decompression successful.")
