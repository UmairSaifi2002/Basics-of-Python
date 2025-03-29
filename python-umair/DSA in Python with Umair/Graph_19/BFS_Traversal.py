# BFS Graph Traversal
# Breadth First Search Traversal for Graphs

from collections import deque

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

    def bfs(self, vertex):
    # Initialize a set to keep track of visited vertices
    visited = set()
    # Add the starting vertex to the visited set
    visited.add(vertex)
    # Initialize a queue with the starting vertex
    # Note: Using deque is more efficient than a list for queue operations
    queue = deque([vertex])
    
    # Continue until the queue is empty
    while queue:
        # Remove and return the leftmost vertex from the queue
        current_vertex = queue.popleft()
        # Print the current vertex (part of BFS traversal result)
        print(current_vertex, end=", ")
        
        # Explore all adjacent vertices of the current vertex
        for adjacent_vertex in self.adjacency_list[current_vertex]:
            # Only process vertices that haven't been visited yet
            if adjacent_vertex not in visited:
                # Mark the adjacent vertex as visited
                visited.add(adjacent_vertex)
                # Add the adjacent vertex to the queue to be processed later
                queue.append(adjacent_vertex)

graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'E')
graph.add_edge('C', 'D')
graph.add_edge('D', 'E')

graph.print_graph()

graph.bfs('A')

'''
Time Complexity Calculation for BFS
To calculate the time complexity of BFS, let's break down the algorithm:

Initialization:

Creating an empty set and adding the starting vertex: O(1)
Creating a queue with one element: O(1)


Main BFS Loop:

The while queue loop can run at most once for each vertex in the graph (since we only enqueue vertices we haven't visited before)
For each vertex, we:

Dequeue it (popleft): O(1) operation with deque
Print it: O(1)
Iterate through all its adjacent vertices:

For each adjacent vertex, we check if it's visited: O(1) with a set
Add it to visited set if not: O(1)
Add it to queue if not visited: O(1)

Let's denote:

V = number of vertices in the graph
E = number of edges in the graph

During the entire BFS:

Each vertex is enqueued and dequeued exactly once: O(V)
For each vertex, we examine all its adjacent vertices (the edges connected to it)
Across all vertices, we examine each edge exactly once in an undirected graph (or twice if you count examining from both endpoints): O(E)

Therefore, the total time complexity is O(V + E).
Space Complexity:

Visited set: O(V)
Queue: At most O(V) elements
Total space complexity: O(V)

The O(V + E) time complexity makes BFS an efficient algorithm for traversing graphs, especially for finding shortest paths in unweighted graphs.
RetryClaude does not have the ability to run the code it generates yet.Claude can make mistakes. Please double-check responses.
'''