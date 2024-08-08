class RabinKarp:
    def __init__(self, pattern, prime=101):
        self.pattern = pattern
        self.prime = prime
        self.base = 256  # Number of characters in the input alphabet
        self.pattern_len = len(pattern)
        self.pattern_hash = self.hash_function(pattern)
        self.current_hash = 0

    def hash_function(self, string):
        """
        Compute hash value for a string.
        
        :param string: Input string
        :return: Hash value (int)
        """
        hash_val = 0
        for char in string:
            hash_val = (self.base * hash_val + ord(char)) % self.prime
        return hash_val

    def search(self, text):
        """
        Search for occurrences of the pattern in the given text.
        
        :param text: Text in which to search for the pattern
        :return: List of starting indices where the pattern is found
        """
        n = len(text)
        results = []

        # Precompute the hash for the initial window of text
        if n < self.pattern_len:
            return results

        self.current_hash = self.hash_function(text[:self.pattern_len])
        pattern_hash = self.pattern_hash
        base_power = pow(self.base, self.pattern_len - 1, self.prime)

        for i in range(n - self.pattern_len + 1):
            if self.current_hash == pattern_hash:
                if text[i:i + self.pattern_len] == self.pattern:
                    results.append(i)

            if i < n - self.pattern_len:
                self.current_hash = (self.base * (self.current_hash - ord(text[i]) * base_power) + ord(text[i + self.pattern_len])) % self.prime
                if self.current_hash < 0:
                    self.current_hash += self.prime

        return results
