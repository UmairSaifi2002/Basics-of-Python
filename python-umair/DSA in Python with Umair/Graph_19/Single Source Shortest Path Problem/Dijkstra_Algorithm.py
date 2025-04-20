# Dijkstra Algorithm

import heapq

class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.min_distance = float('inf')
    
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbours.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []      
    
    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            for edge in actual_vertex.neighbours:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start 
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True




