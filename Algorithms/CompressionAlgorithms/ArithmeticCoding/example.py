from arithmetic_coding import build_probability_table, arithmetic_decode, arithmetic_encode

# Example Usage
if __name__ == "__main__":
    original_text = "hello_world"
    prob_table = build_probability_table(original_text)
    encoded_value = arithmetic_encode(original_text, prob_table)
    print(f"Encoded: {encoded_value}")
    decoded_data = arithmetic_decode(encoded_value, prob_table, len(original_text))
    print(f"Decoded: {decoded_data}")