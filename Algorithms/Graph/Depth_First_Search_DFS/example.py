from depthFirstSearch import Graph

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)

print("DFS Traversal starting from vertex 0:")
print(g.dfs(0))
