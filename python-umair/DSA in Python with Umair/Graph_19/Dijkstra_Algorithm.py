# Dijkstra's Algorithm

class Edge:
    def __init__(self, weight, start_node, target_node):
        self.weight = weight
        self.start_node = start_node
        self.target_node = target_node

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float('inf')

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)

def Dijkstra_Algorithm():
    pass

a = Node('A')
b = Node('B')
print(a < b)
