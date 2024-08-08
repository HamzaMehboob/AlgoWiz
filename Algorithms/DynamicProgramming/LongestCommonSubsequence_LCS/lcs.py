class LCS:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m = len(x)
        self.n = len(y)
        self.dp = [[0] * (self.n + 1) for _ in range(self.m + 1)]

    def compute_lcs(self):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                if self.x[i - 1] == self.y[j - 1]:
                    self.dp[i][j] = self.dp[i - 1][j - 1] + 1
                else:
                    self.dp[i][j] = max(self.dp[i - 1][j], self.dp[i][j - 1])

        return self.dp[self.m][self.n]

    def get_lcs(self):
        lcs = []
        i, j = self.m, self.n

        while i > 0 and j > 0:
            if self.x[i - 1] == self.y[j - 1]:
                lcs.append(self.x[i - 1])
                i -= 1
                j -= 1
            elif self.dp[i - 1][j] > self.dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return ''.join(reversed(lcs))

if __name__ == "__main__":
    x = "ABCBDAB"
    y = "BDCAB"
    lcs = LCS(x, y)
    
    print(f"LCS Length: {lcs.compute_lcs()}")
    print(f"LCS Sequence: {lcs.get_lcs()}")
