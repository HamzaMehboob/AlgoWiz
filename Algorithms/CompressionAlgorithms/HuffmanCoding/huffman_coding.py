
import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None

    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_codes(node, prefix='', codebook=defaultdict()):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encoding(text):
    if not text:
        return "", None

    root = build_huffman_tree(text)
    huffman_codes = build_codes(root)
    encoded_text = ''.join(huffman_codes[char] for char in text)

    return encoded_text, huffman_codes

def huffman_decoding(encoded_text, huffman_codes):
    if not encoded_text or not huffman_codes:
        return ""

    reverse_codes = {code: char for char, code in huffman_codes.items()}
    current_code = ''
    decoded_text = []

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text.append(reverse_codes[current_code])
            current_code = ''

    return ''.join(decoded_text)
