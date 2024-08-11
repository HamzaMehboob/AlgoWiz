import math

class MinimaxAlphaBeta:
    def __init__(self, depth, is_maximizing):
        self.depth = depth
        self.is_maximizing = is_maximizing

    def minimax(self, node, depth, alpha, beta, is_maximizing):
        if depth == 0 or self.is_terminal(node):
            return self.evaluate(node)
        
        if is_maximizing:
            max_eval = -math.inf
            for child in self.get_children(node):
                eval = self.minimax(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for child in self.get_children(node):
                eval = self.minimax(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def is_terminal(self, node):
        # Terminal condition: if node is None or the value is negative
        return node is None or node < 0

    def evaluate(self, node):
        # Simple evaluation function: return the node value
        return node

    def get_children(self, node):
        # Example: generate children nodes by incrementing or decrementing the node value
        return [node - 1, node + 1]
