class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        """Update the value at index (1-based) by delta"""
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        """Get the prefix sum from 1 to index (1-based)"""
        sum_ = 0
        while index > 0:
            sum_ += self.tree[index]
            index -= index & -index
        return sum_

    def range_query(self, left, right):
        """Get the range sum from left to right (1-based)"""
        return self.query(right) - self.query(left - 1)
