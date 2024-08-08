import numpy as np

class GaussianElimination:
    def __init__(self, matrix, b):
        self.A = np.array(matrix, dtype=float)
        self.b = np.array(b, dtype=float)
        self.n = len(b)

    def forward_elimination(self):
        for i in range(self.n):
            # Make the diagonal contain all 1's
            max_row = np.argmax(np.abs(self.A[i:, i])) + i
            if i != max_row:
                self.A[[i, max_row]] = self.A[[max_row, i]]
                self.b[[i, max_row]] = self.b[[max_row, i]]

            for j in range(i + 1, self.n):
                factor = self.A[j, i] / self.A[i, i]
                self.A[j, i:] -= factor * self.A[i, i:]
                self.b[j] -= factor * self.b[i]

    def back_substitution(self):
        x = np.zeros(self.n)
        for i in range(self.n - 1, -1, -1):
            x[i] = (self.b[i] - np.sum(self.A[i, i + 1:] * x[i + 1:])) / self.A[i, i]
        return x

    def solve(self):
        self.forward_elimination()
        return self.back_substitution()
