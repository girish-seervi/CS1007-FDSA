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

    def bfs(self, start):
        visited = set()
        self._bfs_util(start, visited)

    def _bfs_util(self, node, visited):
        if node not in visited:
            print(node, end=" -> ")
            visited.add(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    self._bfs_util(neighbor, visited)

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)

graph.bfs(0)
