from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)
        self.adjacency_list[w].append(v)
    def bfs_shortest_path(self, start_vertex, target_vertex):
        if start_vertex == target_vertex:
            return 0
        queue = deque([(start_vertex, 0)])
        visited = set([start_vertex])
        while queue:
            vertex, distance = queue.popleft()
            for neighbour in self.adjacency_list[vertex]:
                if neighbour == target_vertex:
                    return distance + 1
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, distance + 1))
        return -1

class SocialNetwork:
    def __init__(self):
        self.graph = Graph()
    def add_friendship(self, user1, user2):
        self.graph.add_edge(user1, user2)
    def degrees_of_separation(self, user1, user2):
        return self.graph.bfs_shortest_path(user1, user2)

network = SocialNetwork()
network.add_friendship(0, 1)
network.add_friendship(0, 2)
network.add_friendship(1, 3)
network.add_friendship(2, 4)
network.add_friendship(3, 5)
network.add_friendship(4, 5)

print("Degrees of separation between 0 and 5:", network.degrees_of_separation(0, 5))
