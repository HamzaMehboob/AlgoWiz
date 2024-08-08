from graph import GraphAdjList, GraphAdjMatrix

def example_adj_list():
    print("Adjacency List:")
    graph_list = GraphAdjList()
    graph_list.add_edge(0, 1)
    graph_list.add_edge(1, 2)
    graph_list.add_edge(2, 3)
    graph_list.add_edge(3, 0)
    graph_list.display()

def example_adj_matrix():
    print("\nAdjacency Matrix:")
    size = 4
    graph_matrix = GraphAdjMatrix(size)
    graph_matrix.add_edge(0, 1)
    graph_matrix.add_edge(1, 2)
    graph_matrix.add_edge(2, 3)
    graph_matrix.add_edge(3, 0)
    graph_matrix.display()

def main():
    example_adj_list()
    example_adj_matrix()

if __name__ == "__main__":
    main()
