# Bellman Ford Algorithm

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
    
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def add_nodes(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print('Vertex Distance from Source')
        for key, value in dist.items():
            print(f'{key} : {value}')
    
    def bellmanFord(self, src):
        dist = {i : float('Inf') for i in self.nodes}
        dist[src] = 0
        for _ in range(self.V-1):
            for s, d, w in self.graph:
                if dist[s] != float('Inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float('Inf') and dist[s] + w < dist[d]:
                print('Negative Cycle Detected.')
                return
        
        self.print_solution(dist)

g = Graph(5)
g.add_nodes('A')
g.add_nodes('B')
g.add_nodes('C')
g.add_nodes('D')
g.add_nodes('E')

g.add_edge('A', 'C', 6)
g.add_edge('A', 'D', 6)
g.add_edge('B', 'A', 3)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'C', 2)
g.add_edge('D', 'B', 1)
g.add_edge('E', 'B', 4)
g.add_edge('E', 'D', 2)

g.bellmanFord('E')
