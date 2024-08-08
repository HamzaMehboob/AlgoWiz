from breathFirstSearch import Graph

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)

print("BFS Traversal starting from vertex 0:")
print(g.bfs(0))
