class Graph:
    def __init__(self):
        self.adj_list = {}
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
    def detect_cycle(self):
        visited = set()
        def _dfs(v, rec_stack):
            visited.add(v)
            rec_stack.add(v)
            for neighbour in self.adj_list.get(v, []):
                if neighbour not in visited:
                    if _dfs(neighbour, rec_stack):
                        return True
                elif neighbour in rec_stack:
                    return True
            rec_stack.remove(v)
            return False
        for vertex in self.adj_list:
            if vertex not in visited:
                if _dfs(vertex, set()):
                    return True
        return False

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 0)

print(graph.detect_cycle())
