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