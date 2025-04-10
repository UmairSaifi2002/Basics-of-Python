# Graph Algorithm

# Let's Learn about Something about Graphs

# What is Graph? Why do we need it?
# a graph is a non-linear data structure consisting of nodes or vertices connected by edges. 
# Each node may have multiple edges connected to it, and each edge may have a weight or label associated with it. 
# Graphs can be used to represent relationships between objects, such as friendships between people, cities connected by roads, or websites linked to each other.
# Graphs are essential in many fields, including:
# 1. Computer Networks: Graphs help design and optimize network topologies.
# 2. Social Network Analysis: Graphs model relationships between people, groups, or organizations.
# 3. Traffic and Transportation: Graphs optimize routes and traffic flow.
# 4. Recommendation Systems: Graphs help predict user preferences.
# 5. Data Analysis: Graphs visualize and analyze complex data relationships.
# 6. Machine Learning: Graphs are used in neural networks and deep learning.
# 7. Game Development: Graphs model game environments and AI behaviors.

# Types of Graphs, Graph Representtion
# There are different types of Graphs
# 1, Directed Graphs
# 2, Un-Directed Graphs
# 3, Weighted Graphs
# 4, Un-Weighted Graphs

# Traversal of Graphs. (BFS and DFS)
# BFS :- Breath First Search
# DFS :- Depth First Search

# Topological Sorting

# Single Source Shortest Path(BFS, Dijkstra, and Bellman Ford)

# All Pairs Shortest Path(BFS, Dijsktra, BellmanFord, and Floyd Warshall Algorithm)

# Minimum Spanning Tree(Kruskal, and Prim's Algorithm)



# Now Create a Basic Structure of Graph
class Graph:
    def __init__(self):
        # Creates empty graph: {vertex: [connected_vertices]}
        self.adjacencyList = {}
    
    def add_vertex(self, vertex):
        # Adds new vertex if not already exists
        if vertex not in self.adjacencyList.keys():
            self.adjacencyList[vertex] = []  # Start with no connections
            return True
        return False  # Vertex already exists
    
    def add_edge(self, v1, v2):
        # Connects two vertices (makes them neighbors)
        if v1 in self.adjacencyList.keys() and v2 in self.adjacencyList.keys():
            self.adjacencyList[v1].append(v2)  # v2 added to v1's connections
            self.adjacencyList[v2].append(v1)  # v1 added to v2's connections
            return True
        return False  # One or both vertices don't exist
    
    def printList(self):
        # Shows the graph: Vertex -> [all connected vertices]
        for v in self.adjacencyList:
            print(f'{v} : {self.adjacencyList[v]}')
    
    def remove_edge(self, v1, v2):
        # Removes connection between two vertices
        if v1 in self.adjacencyList.keys() and v2 in self.adjacencyList.keys():
            self.adjacencyList[v1].remove(v2)  # Remove v2 from v1's connections
            self.adjacencyList[v2].remove(v1)  # Remove v1 from v2's connections
            return True
        return False  # One or both vertices don't exist
    
    def remove_vertex(self, v):
        # Completely removes a vertex and all its connections
        if v in self.adjacencyList.keys():
            # First remove all edges to this vertex from other vertices
            for otherVertex in self.adjacencyList[v]:
                self.adjacencyList[otherVertex].remove(v)  # Remove v from each neighbor's list
            del self.adjacencyList[v]  # Delete the vertex itself
            return True
        return False  # Vertex doesn't exist


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.printList()

print('---------- Removing an Edge ----------')
g.remove_edge('B', 'C')
g.printList()

print('---------- Removing a Vertex ----------')
g.remove_vertex('D')
g.printList()

