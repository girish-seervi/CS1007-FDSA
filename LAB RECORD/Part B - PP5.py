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
    def dfs(self, start):
        visited = set()
        self._dfs_util(start, visited)
    def _dfs_util(self, node, visited):
        if node not in visited:
            print(node, end = ' -> ')
            visited.add(node)
            for neighbour in self.adj_list[node]:
                self._dfs_util(neighbour, visited)

graph = Graph()

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)

print("DFS Traversal starting from vertex 0:")
graph.dfs(0)
