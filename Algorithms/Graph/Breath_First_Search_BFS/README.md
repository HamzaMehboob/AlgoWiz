# Breadth-First Search (BFS) Algorithm

This repository contains an implementation of the Breadth-First Search (BFS) algorithm in Python. BFS is an algorithm for traversing or searching tree or graph data structures. It starts at the root (or an arbitrary node in the case of a graph) and explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

## Introduction

Breadth-First Search is commonly used for finding the shortest path in an unweighted graph, performing level-order traversal, and more. This implementation supports undirected graphs.

## Features

- Implements BFS for undirected graphs.
- Handles graphs with multiple vertices and edges.
- Provides an easy-to-use interface for adding edges and performing BFS traversal.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/Graph/Breath_First_Search_BFS
    ```

2. Run the example script:
    ```sh
    python example.py
    ```

## Example

Here is an example usage of the BFS algorithm:

```python
from bfs import Graph

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)

print("BFS Traversal starting from vertex 0:")
print(g.bfs(0))

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com