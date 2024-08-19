import random

class ContextMixingCompressor:
    def __init__(self, order=2):
        self.order = order
        self.context = {}
        self.total_context = {}

    def _update_context(self, context_str, symbol):
        if context_str not in self.context:
            self.context[context_str] = [0] * 256
        if context_str not in self.total_context:
            self.total_context[context_str] = 0
        self.context[context_str][ord(symbol)] += 1
        self.total_context[context_str] += 1

    def _predict_next(self, context_str):
        if context_str not in self.context:
            return random.choice(range(256))
        total = self.total_context[context_str]
        probs = [count / total for count in self.context[context_str]]
        return probs.index(max(probs))

    def compress(self, data):
        compressed = []
        for i in range(len(data)):
            context_str = data[max(0, i - self.order):i]
            prediction = self._predict_next(context_str)
            compressed.append(prediction)
            self._update_context(context_str, data[i])
        return compressed

    def decompress(self, compressed_data):
        decompressed = []
        for i in range(len(compressed_data)):
            context_str = ''.join(decompressed[max(0, i - self.order):i])
            predicted_symbol = chr(self._predict_next(context_str))
            decompressed.append(predicted_symbol)
            self._update_context(context_str, predicted_symbol)
        return ''.join(decompressed)

# Example Usage
if __name__ == "__main__":
    original_text = "abracadabra"
    
    compressor = ContextMixingCompressor(order=2)
    compressed_data = compressor.compress(original_text)
    print(f"Compressed Data: {compressed_data}")
    
    decompressed_data = compressor.decompress(compressed_data)
    print(f"Decompressed Data: {decompressed_data}")
    
    # Verify correctness
    assert original_text == decompressed_data, "Context Mixing compression and decompression failed."
    print("Context Mixing compression and decompression successful.")
