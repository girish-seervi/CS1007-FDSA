class Graph:
    def __init__(self):
        self.adj_list = {}
    def add_edge(self, v, w):
        if v not in self.adj_list:
            self.adj_list[v] = []
        if w not in self.adj_list:
            self.adj_list[w] = []
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)
    def print_graph(self):
        for vertex in sorted(self.adj_list.keys()):
            print(f"{vertex}: {sorted(self.adj_list[vertex])}")

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 0)
graph.print_graph()
