class GraphAdjList:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph; remove for directed graph

    def display(self):
        for node, edges in self.graph.items():
            print(f"{node}: {', '.join(map(str, edges))}")

class GraphAdjMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # For undirected graph; remove for directed graph

    def display(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))
