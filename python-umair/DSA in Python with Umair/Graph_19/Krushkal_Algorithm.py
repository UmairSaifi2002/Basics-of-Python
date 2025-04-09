class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        # self.parent = parent
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[xroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []
    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
    def addNode(self, value):
        self.nodes.append(value)
    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print(f"{s} - {d} : {w}")
    def KrushkalAlgorithm(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printSolution(s, d, w)


G = Graph(5)

G.addNode("A")
G.addNode("B")
G.addNode("C")
G.addNode("D")
G.addNode("E")

G.addEdge("A", "B", 5)
G.addEdge("A", "C", 13)
G.addEdge("A", "E", 15)
G.addEdge("B", "A", 5)
G.addEdge("B", "C", 10)
G.addEdge("B", "D", 8)
G.addEdge("C", "A", 13)
G.addEdge("C", "B", 10)
G.addEdge("C", "E", 20)
G.addEdge("C", "D", 6)
G.addEdge("D", "B", 8)
G.addEdge("D", "C", 6)
G.addEdge("E", "A", 15)
G.addEdge("E", "C", 20)

G.KrushkalAlgorithm()

