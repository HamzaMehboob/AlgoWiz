from collections import defaultdict

def build_probability_table(data):
    """Build a cumulative probability table for range coding."""
    freq_table = defaultdict(int)
    for symbol in data:
        freq_table[symbol] += 1
    
    total = sum(freq_table.values())
    prob_table = {}
    low = 0.0

    for symbol, freq in sorted(freq_table.items()):
        high = low + freq / total
        prob_table[symbol] = (low, high)
        low = high

    return prob_table

def range_encode(data, prob_table):
    """Range Encoding algorithm."""
    low, high = 0.0, 1.0

    for symbol in data:
        range_ = high - low
        high = low + range_ * prob_table[symbol][1]
        low = low + range_ * prob_table[symbol][0]

    return (low + high) / 2

def range_decode(encoded_value, prob_table, length):
    """Range Decoding algorithm."""
    decoded_data = []
    low, high = 0.0, 1.0

    for _ in range(length):
        range_ = high - low
        scaled_value = (encoded_value - low) / range_

        for symbol, (low_prob, high_prob) in prob_table.items():
            if low_prob <= scaled_value < high_prob:
                decoded_data.append(symbol)
                high = low + range_ * high_prob
                low = low + range_ * low_prob
                break

    return ''.join(decoded_data)

# Example Usage
if __name__ == "__main__":
    original_text = "hello_world"
    prob_table = build_probability_table(original_text)
    encoded_value = range_encode(original_text, prob_table)
    print(f"Encoded Value: {encoded_value}")

    decoded_data = range_decode(encoded_value, prob_table, len(original_text))
    print(f"Decoded Data: {decoded_data}")
