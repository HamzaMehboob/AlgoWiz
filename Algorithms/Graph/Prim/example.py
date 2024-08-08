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
