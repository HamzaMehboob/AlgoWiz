from bwt import bwt_transform, bwt_inverse

# Example text
text = "banana"

# Apply BWT
transformed, index = bwt_transform(text)
print(f"Original Text: {text}")
print(f"Transformed Text: {transformed}, Index: {index}")

# Inverse BWT
reconstructed = bwt_inverse(transformed, index)
print(f"Reconstructed Text: {reconstructed}")

# Verify correctness
assert text == reconstructed, "BWT transformation and inversion failed."
print("BWT transformation and inversion successful.")
