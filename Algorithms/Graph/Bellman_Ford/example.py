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
