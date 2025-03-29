class Graph:
    def __init__(self, G_Dict=None):
        if G_Dict is None:
            G_Dict = {}
        self.G_Dict = G_Dict

    def add_edge(self, vertex, edge):
        self.G_Dict[vertex].append(edge)

myDict = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','E'],
    'D' : ['B','E'],
    'E' : ['D','F','C'],
    'F' : ['D','E']
}

myGraph = Graph(myDict)
print(myGraph.G_Dict)
myGraph.add_edge('D','F')
print(myGraph.G_Dict)
