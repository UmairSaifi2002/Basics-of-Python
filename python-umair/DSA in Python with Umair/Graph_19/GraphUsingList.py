# Graph using adjacency list
class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        # Keys are vertices and values are lists of adjacent vertices
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        # Add a new vertex to the graph if it doesn't already exist
        if vertex not in self.adjacency_list.keys():
            # Initialize with empty list as no edges yet
            self.adjacency_list[vertex] = []
            return True
        # Return False if vertex already exists
        return False
    
    def add_edge(self, vertex1, vertex2):
        # Add an edge between two vertices if both vertices exist
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            # Add vertex2 to vertex1's adjacency list
            self.adjacency_list[vertex1].append(vertex2)
            # Add vertex1 to vertex2's adjacency list (undirected graph)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        # Return False if either vertex doesn't exist
        return False
    
    def remove_edge(self, vertex1, vertex2):
        # Remove an edge between two vertices if both vertices exist
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                # Remove vertex2 from vertex1's adjacency list
                self.adjacency_list[vertex1].remove(vertex2)
                # Remove vertex1 from vertex2's adjacency list
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                # Exception occurs if the edge doesn't exist
                pass
        # Return False if vertices don't exist or edge removal fails
        return False
    
    def remove_vertex(self, vertex):
        # Remove a vertex and all its edges from the graph
        if vertex in self.adjacency_list.keys():
            # Get list of adjacent vertices
            l = self.adjacency_list[vertex]
            # For each adjacent vertex, remove this vertex from their adjacency lists
            for i in l:
                self.adjacency_list[i].remove(vertex)
            # Remove the vertex from the graph
            self.adjacency_list.pop(vertex)
            return True
        # Return False if vertex doesn't exist
        return False
    
    def print_graph(self):
        # Print the graph as an adjacency list
        for vertex in self.adjacency_list.keys():
            print(vertex, " -> ", self.adjacency_list[vertex])

# Create a new graph
graph = Graph()

# Add vertices to the graph
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

# Add edges between vertices
graph.add_edge('A', 'B')  # Connect A and B
graph.add_edge('A', 'C')  # Connect A and C
graph.add_edge('B', 'C')  # Connect B and C
graph.add_edge('C', 'D')  # Connect C and D

# Print the initial graph structure
graph.print_graph()

print("After removing edge between A and C")
# Remove the edge between A and C
graph.remove_edge('A', 'C')
# Try to remove an edge that doesn't exist (A-D)
graph.remove_edge('A', 'D')
# Print the updated graph
graph.print_graph()

print("After removing vertex D")
# Remove vertex D and all its edges
graph.remove_vertex('D')
# Print the final graph
graph.print_graph()