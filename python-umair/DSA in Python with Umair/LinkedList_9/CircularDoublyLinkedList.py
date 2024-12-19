class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = Node

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 

