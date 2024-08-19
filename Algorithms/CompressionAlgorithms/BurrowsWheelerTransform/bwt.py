def bwt_transform(text):
    """Apply Burrows-Wheeler Transform (BWT) to the input text."""
    n = len(text)
    m = sorted([text[i:] + text[:i] for i in range(n)])
    last_column = ''.join(row[-1] for row in m)
    return last_column, m.index(text)

def bwt_inverse(last_column, index):
    """Inverse Burrows-Wheeler Transform (BWT) to reconstruct the original text."""
    n = len(last_column)
    table = [""] * n
    
    for _ in range(n):
        table = sorted([last_column[i] + table[i] for i in range(n)])
    
    return table[index]

# Example Usage
if __name__ == "__main__":
    original_text = "banana"
    transformed, index = bwt_transform(original_text)
    print(f"Transformed: {transformed}, Index: {index}")
    
    reconstructed = bwt_inverse(transformed, index)
    print(f"Reconstructed: {reconstructed}")
