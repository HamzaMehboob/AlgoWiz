# Bellman-Ford Algorithm

## Overview
The Bellman-Ford algorithm is used for finding the shortest path from a single source vertex to all other vertices in a weighted graph. It is capable of handling graphs with negative weight edges, making it more versatile than Dijkstra's algorithm.

## Features
- **Handles Negative Weights**: Unlike Dijkstra's algorithm, Bellman-Ford can manage negative weights in the graph.
- **Detects Negative Cycles**: The algorithm can also detect negative weight cycles.

## How It Works
The algorithm works by iteratively relaxing all edges in the graph. It does this `V-1` times (where `V` is the number of vertices). If a shorter path is found, the algorithm updates the distance. After `V-1` iterations, if a shorter path is still found, it indicates the presence of a negative weight cycle.

## Usage


1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/Graph/Bellman_Ford
    ```

2. Run the example script:
    ```sh
    python example.py
    ```

### Example
```python
from bellman_ford import BellmanFord

def main():
    g = BellmanFord(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    source_vertex = 0
    distances = g.run(source_vertex)

    if distances is not None:
        print(f"Vertex Distance from Source {source_vertex}")
        for i, d in enumerate(distances):
            print(f"{i}\t\t{d}")

if __name__ == "__main__":
    main()
