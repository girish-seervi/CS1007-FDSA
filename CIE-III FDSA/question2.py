class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[v].append(u)

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.display()