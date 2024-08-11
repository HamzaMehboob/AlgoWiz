from minimax_alpha_beta import MinimaxAlphaBeta
import math

def main():
    # Example usage
    depth = 3  # Depth of the search
    is_maximizing = True  # Assuming the root node is a maximizing node

    # Create an instance of the algorithm
    minimax = MinimaxAlphaBeta(depth, is_maximizing)

    # Example node (starting value)
    node = 0  # Replace with actual starting value
    result = minimax.minimax(node, depth, -math.inf, math.inf, is_maximizing)

    print("Optimal value:", result)

if __name__ == "__main__":
    main()
