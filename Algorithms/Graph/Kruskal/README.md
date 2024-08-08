# Kruskal's Algorithm

This repository contains an implementation of Kruskal's Algorithm in Python. Kruskal's Algorithm is a popular algorithm used to find the Minimum Spanning Tree (MST) of a graph. The algorithm finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

## Introduction

Kruskal's algorithm is a greedy algorithm that finds the MST by selecting the smallest weight edge that does not form a cycle with the previously selected edges. It is widely used in network design, such as designing a telecommunications network or a computer network.

## Features

- Efficiently finds the Minimum Spanning Tree (MST) of a graph.
- Handles graphs with weighted edges.
- Uses Disjoint Set Union (DSU) to detect cycles.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/Graph/Kruskal
    ```

2. Run the example script:
    ```sh
    python kruskal.py
    ```

## Example

Here is an example usage of the algorithm:

```python
from kruskal import Graph

g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(1, 2, 3)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst = g.kruskal()
print("Edges in the constructed MST:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com