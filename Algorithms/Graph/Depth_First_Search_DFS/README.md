# Depth-First Search (DFS) Algorithm

This repository contains an implementation of the Depth-First Search (DFS) algorithm in Python. DFS is an algorithm for traversing or searching tree or graph data structures. It starts at the root (or an arbitrary node in the case of a graph) and explores as far as possible along each branch before backtracking.

## Introduction

Depth-First Search is commonly used for exploring all nodes and edges in a graph, solving puzzles, and finding paths in mazes. This implementation supports undirected graphs.

## Features

- Implements DFS for undirected graphs.
- Handles graphs with multiple vertices and edges.
- Provides an easy-to-use interface for adding edges and performing DFS traversal.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/Graph/Depth_First_Search_DFS
    ```

2. Run the example script:
    ```sh
    python example.py
    ```

## Example

Here is an example usage of the DFS algorithm:

```python
from dfs import Graph

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)

print("DFS Traversal starting from vertex 0:")
print(g.dfs(0))

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com