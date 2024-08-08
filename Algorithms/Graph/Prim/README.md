# Prim's Algorithm

This repository contains an implementation of Prim's Algorithm in Python. Prim's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, undirected graph with weighted edges.

## Introduction

Prim's algorithm starts with a single vertex and continuously adds the smallest edge that connects a vertex in the MST to a vertex outside of the MST, until all vertices are included. It is widely used in network design, such as designing communication networks and electrical grids.

## Features

- Efficiently finds the Minimum Spanning Tree (MST) of a connected, undirected graph.
- Handles graphs with weighted edges.
- Greedy approach that builds the MST by adding one vertex at a time.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/Graph/Prim
    ```

2. Run the example script:
    ```sh
    python example.py
    ```

## Example

Here is an example usage of the algorithm:

```python
from prim import Graph

g = Graph(6)
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 7)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 4)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 6)
g.add_edge(3, 5, 8)
g.add_edge(4, 5, 9)

parent = g.prim_mst()
g.print_mst(parent)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com