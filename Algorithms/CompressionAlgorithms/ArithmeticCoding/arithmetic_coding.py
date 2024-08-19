from collections import defaultdict

def arithmetic_encode(data, probability_table):
    """Arithmetic Encoding compression."""
    low = 0.0
    high = 1.0

    for symbol in data:
        range_ = high - low
        high = low + range_ * probability_table[symbol][1]
        low = low + range_ * probability_table[symbol][0]

    return (low + high) / 2

def arithmetic_decode(encoded_value, probability_table, length):
    """Arithmetic Encoding decompression."""
    decoded_data = []
    low = 0.0
    high = 1.0

    for _ in range(length):
        range_ = high - low
        scaled_value = (encoded_value - low) / range_

        for symbol, (low_prob, high_prob) in probability_table.items():
            if low_prob <= scaled_value < high_prob:
                decoded_data.append(symbol)
                high = low + range_ * high_prob
                low = low + range_ * low_prob
                break

    return ''.join(decoded_data)

def build_probability_table(data):
    """Build a probability table for arithmetic coding."""
    freq_table = defaultdict(int)

    for symbol in data:
        freq_table[symbol] += 1

    total = sum(freq_table.values())
    low = 0.0

    probability_table = {}
    for symbol, freq in freq_table.items():
        high = low + freq / total
        probability_table[symbol] = (low, high)
        low = high

    return probability_table


