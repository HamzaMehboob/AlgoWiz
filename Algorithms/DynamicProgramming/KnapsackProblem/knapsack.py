class Knapsack:
    def __init__(self, capacity, weights, values):
        self.capacity = capacity
        self.weights = weights
        self.values = values
        self.n = len(weights)
        self.dp = [[0] * (capacity + 1) for _ in range(self.n + 1)]

    def solve(self):
        # Build the DP table
        for i in range(1, self.n + 1):
            for w in range(1, self.capacity + 1):
                if self.weights[i - 1] <= w:
                    self.dp[i][w] = max(self.dp[i - 1][w], self.dp[i - 1][w - self.weights[i - 1]] + self.values[i - 1])
                else:
                    self.dp[i][w] = self.dp[i - 1][w]
        
        return self.dp[self.n][self.capacity]

    def get_selected_items(self):
        selected_items = []
        w = self.capacity
        for i in range(self.n, 0, -1):
            if self.dp[i][w] != self.dp[i - 1][w]:
                selected_items.append(i - 1)
                w -= self.weights[i - 1]
        return selected_items

if __name__ == "__main__":
    capacity = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]

    knapsack = Knapsack(capacity, weights, values)
    
    print("Maximum value in Knapsack:", knapsack.solve())
    print("Selected item indices:", knapsack.get_selected_items())
