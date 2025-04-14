# Graph
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

    # BFS :- Breath First Search Traversal
    def bfs(self, v):
        visited = set()
        visited.add(v)
        queue = [v]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex,end=', ')
            for adjacent_vertex in self.adjacencyList[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
        print()
    
    # DFS :- Depth Fiirst Search
    def dfs(self, v):
        visited = set()
        stack = [v]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex,end=', ')
            for adjacent_vertex in self.adjacencyList[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)
        print()

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'D')
g.add_edge('B', 'E')
g.add_edge('B', 'D')
g.add_edge('C', 'B')
g.add_edge('C', 'D')
g.add_edge('E', 'D')
# BFS Traversal
print('BFS Traversal')
g.bfs('A')
# DFS Traversal
print('DFS Traversal')
g.dfs('A')

print(g.adjacencyList)
