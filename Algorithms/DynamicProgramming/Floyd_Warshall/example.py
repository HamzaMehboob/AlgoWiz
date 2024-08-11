import numpy as np
from floyd_warshall import FloydWarshall

def main():
    # Example graph as an adjacency matrix
    graph = [
        [0, 3, np.inf, np.inf, np.inf, np.inf],
        [2, 0, np.inf, np.inf, np.inf, 5],
        [np.inf, 7, 0, np.inf, np.inf, 1],
        [6, np.inf, 2, 0, np.inf, np.inf],
        [np.inf, np.inf, np.inf, 1, 0, 2],
        [np.inf, np.inf, np.inf, np.inf, 4, 0]
    ]
    
    fw = FloydWarshall(graph)
    shortest_paths = fw.run()
    
    print("Shortest paths matrix:")
    print(shortest_paths)

if __name__ == "__main__":
    main()
