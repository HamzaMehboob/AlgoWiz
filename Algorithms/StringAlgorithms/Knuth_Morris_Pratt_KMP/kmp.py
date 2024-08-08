class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lps = self.compute_lps_array(pattern)

    def compute_lps_array(self, pattern):
        """
        Compute the Longest Prefix Suffix (LPS) array for the pattern.
        
        :param pattern: The pattern for which to compute the LPS array
        :return: LPS array (list of integers)
        """
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def search(self, text):
        """
        Search for occurrences of the pattern in the given text using KMP algorithm.
        
        :param text: Text in which to search for the pattern
        :return: List of starting indices where the pattern is found
        """
        m = len(self.pattern)
        n = len(text)
        lps = self.lps
        i = 0
        j = 0
        results = []

        while i < n:
            if self.pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                results.append(i - j)
                j = lps[j - 1]
            elif i < n and self.pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return results
