class Fibonacci:
    def __init__(self, n):
        self.n = n

    def generate(self):
        sequence = []
        a, b = 0, 1
        while len(sequence) < self.n:
            sequence.append(a)
            a, b = b, a + b
        return sequence

if __name__ == "__main__":
    n = 10  # Number of Fibonacci numbers to generate
    fib = Fibonacci(n)
    print(f"First {n} Fibonacci numbers: {fib.generate()}")
