from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, visited):
        visited[start] = True
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def dfs_traversal(self, start):
        visited = [False] * len(self.graph)
        self.dfs(start, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal (starting from vertex 2):")
g.dfs_traversal(2)
