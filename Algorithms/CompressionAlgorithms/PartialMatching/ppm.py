from collections import defaultdict, Counter

class PPMNode:
    def __init__(self, char=None):
        self.char = char
        self.children = defaultdict(PPMNode)
        self.count = 0

def ppm_train(text, order):
    """Train the PPM model on the given text."""
    root = PPMNode()
    for i in range(len(text)):
        context = ''
        for j in range(i, min(i + order, len(text))):
            char = text[j]
            node = root
            for k in range(i, j):
                if text[k] not in node.children:
                    node.children[text[k]] = PPMNode(text[k])
                node = node.children[text[k]]
            if char not in node.children:
                node.children[char] = PPMNode(char)
            node = node.children[char]
            node.count += 1
    return root

def ppm_compress(text, order, model):
    """Compress the text using the PPM model."""
    encoded_text = []
    context = ''
    
    for char in text:
        node = model
        for c in context:
            if c in node.children:
                node = node.children[c]
            else:
                node = None
                break
        if node and char in node.children:
            encoded_text.append(node.children[char].count)
        else:
            encoded_text.append(0)
        context = (context + char)[-order:]
    
    return encoded_text

def ppm_decompress(encoded_text, order, model):
    """Decompress the text using the PPM model."""
    decoded_text = []
    context = ''
    
    for count in encoded_text:
        node = model
        for c in context:
            if c in node.children:
                node = node.children[c]
            else:
                node = None
                break
        if node:
            found = False
            for char, child in node.children.items():
                if child.count == count:
                    decoded_text.append(char)
                    context = (context + char)[-order:]
                    found = True
                    break
            if not found:
                decoded_text.append('')
        else:
            decoded_text.append('')
    
    return ''.join(decoded_text)

# Example Usage
if __name__ == "__main__":
    original_text = "abracadabra"
    order = 2
    
    model = ppm_train(original_text, order)
    compressed = ppm_compress(original_text, order, model)
    print(f"Compressed: {compressed}")
    
    decompressed = ppm_decompress(compressed, order, model)
    print(f"Decompressed: {decompressed}")
