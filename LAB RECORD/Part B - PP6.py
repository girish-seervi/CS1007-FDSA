class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def detect_cycle(self):
        visited = set()

        def _dfs(v, parent):
            visited.add(v)
            for neighbour in self.adj_list[v]:
                if neighbour not in visited:
                    if _dfs(neighbour, v):
                        return True
                elif neighbour != parent:
                    return True
            return False

        for vertex in self.adj_list:
            if vertex not in visited:
                if _dfs(vertex, None):
                    return True
        return False


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(0, 4)

# Check for cycle
print(graph.detect_cycle())
