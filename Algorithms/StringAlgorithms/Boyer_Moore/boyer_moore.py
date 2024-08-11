# boyer_moore.py

class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.bad_char_shift = self._compute_bad_char_shift()
        self.good_suffix_shift = self._compute_good_suffix_shift()
        
    def _compute_bad_char_shift(self):
        bad_char_shift = {}
        pattern_length = len(self.pattern)
        for i, char in enumerate(self.pattern):
            bad_char_shift[char] = pattern_length - i - 1
        return bad_char_shift

    def _compute_good_suffix_shift(self):
        pattern_length = len(self.pattern)
        good_suffix_shift = [0] * pattern_length
        last_prefix_position = pattern_length
        
        for i in range(pattern_length - 1, -1, -1):
            if self._is_prefix(i + 1):
                last_prefix_position = i + 1
            good_suffix_shift[pattern_length - i - 1] = last_prefix_position - i + pattern_length - 1

        for i in range(pattern_length - 1):
            len_suffix = self._suffix_length(i)
            good_suffix_shift[len_suffix] = pattern_length - i - 1 + len_suffix
        
        return good_suffix_shift

    def _is_prefix(self, index):
        pattern_length = len(self.pattern)
        i = index
        j = 0
        while i < pattern_length:
            if self.pattern[i] != self.pattern[j]:
                return False
            i += 1
            j += 1
        return True

    def _suffix_length(self, index):
        pattern_length = len(self.pattern)
        length = 0
        i = index
        j = pattern_length - 1
        while i >= 0 and self.pattern[i] == self.pattern[j]:
            length += 1
            i -= 1
            j -= 1
        return length

    def search(self, text):
        pattern_length = len(self.pattern)
        text_length = len(text)
        i = 0
        
        while i <= text_length - pattern_length:
            j = pattern_length - 1
            while j >= 0 and text[i + j] == self.pattern[j]:
                j -= 1
            if j < 0:
                return i
            i += max(self.bad_char_shift.get(text[i + pattern_length - 1], pattern_length), 
                     self.good_suffix_shift[pattern_length - j - 1])
        return -1
