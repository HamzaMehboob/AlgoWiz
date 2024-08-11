import numpy as np

class FloydWarshall:
    def __init__(self, graph):
        self.graph = np.array(graph, dtype=float)
        self.num_vertices = self.graph.shape[0]

    def run(self):
        dist = np.copy(self.graph)
        
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        return dist
