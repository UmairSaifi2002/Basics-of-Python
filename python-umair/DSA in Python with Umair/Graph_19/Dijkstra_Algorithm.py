# Dijkstra's Algorithm
import heapq
class Edge:
    def __init__(self, weight, start_node, target_node):
        self.weight = weight
        self.start_node = start_node
        self.target_node = target_node

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        # Previous node that we come to this node
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float('inf')

    # this a function is to calculate less than function
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)

class Dijkstra_Algorithm:
    def __init__(self):
        self.heap = []

    def calculate(self,start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            # pop elment with its lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider the neighbors
            for edge in actual_vertex.neighbors:
                start = edge.start_node
                target = edge.target_node
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance :
                    target.min_distance = new_distance
                    target.predecessor = start
                    # Update the Heap
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True
    
    def get_shortest_path(self, vertex):
        print(f'The shortest path to the vertex is : {vertex.min_distance}')
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=' ')
            actual_vertex = actual_vertex.predecessor


# a = Node('A')
# b = Node('B')
# print(a > b)

# Step 1 - Create Nodes
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')

nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(16, nodeE)
nodeB.add_edge(13, nodeF)
nodeB.add_edge(5, nodeD)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(14, nodeG)

algorithm = Dijkstra_Algorithm()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeG)
