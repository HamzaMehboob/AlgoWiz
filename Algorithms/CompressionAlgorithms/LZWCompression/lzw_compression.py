class LZW:
    def __init__(self):
        self.max_table_size = 2**12  # Example size
        self.table = {chr(i): i for i in range(256)}

    def compress(self, input_string):
        current_string = ""
        compressed_data = []
        code = 256  # Next code value

        for char in input_string:
            current_string += char
            if current_string not in self.table:
                compressed_data.append(self.table[current_string[:-1]])
                if len(self.table) < self.max_table_size:
                    self.table[current_string] = code
                    code += 1
                current_string = char

        if current_string:
            compressed_data.append(self.table[current_string])

        return compressed_data

    def decompress(self, compressed_data):
        reverse_table = {i: chr(i) for i in range(256)}
        current_code = compressed_data.pop(0)
        current_string = reverse_table[current_code]
        decompressed_data = [current_string]

        code = 256

        for code in compressed_data:
            if code in reverse_table:
                entry = reverse_table[code]
            elif code == len(reverse_table):
                entry = current_string + current_string[0]

            decompressed_data.append(entry)

            reverse_table[len(reverse_table)] = current_string + entry[0]
            current_string = entry

        return ''.join(decompressed_data)
