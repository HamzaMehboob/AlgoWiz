from gaussian_elimination import GaussianElimination

def main():
    # Example matrix and right-hand side vector
    matrix = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    gaussian = GaussianElimination(matrix, b)
    solution = gaussian.solve()

    print("Matrix A:")
    for row in matrix:
        print(row)

    print("\nRight-hand side vector b:")
    print(b)

    print("\nSolution vector x:")
    print(solution)

if __name__ == "__main__":
    main()
