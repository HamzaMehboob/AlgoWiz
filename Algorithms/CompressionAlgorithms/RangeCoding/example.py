from range_coding import build_probability_table, range_encode, range_decode

# Example text
original_text = "hello_world"

# Build probability table
prob_table = build_probability_table(original_text)

# Encode the text
encoded_value = range_encode(original_text, prob_table)
print(f"Original Text: {original_text}")
print(f"Encoded Value: {encoded_value}")

# Decode the text
decoded_text = range_decode(encoded_value, prob_table, len(original_text))
print(f"Decoded Text: {decoded_text}")

# Verify correctness
assert original_text == decoded_text, "Range coding transformation and inversion failed."
print("Range coding transformation and inversion successful.")
