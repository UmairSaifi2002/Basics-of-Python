# Here we gonna implement Queue using LinkedList.
# We will create a node class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
    
# now we create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
    
# Now we will create Queue class.
class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
    def __str__(self):
        q = [str(val) for val in self.LinkedList ]
        return ' '.join(q)
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    def enqueue(self, value):
        node = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node
    def dequeue(self):
        if self.isEmpty():
            return "The Queue is empty."
        else:
            if self.LinkedList.head.next == None:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                node = self.LinkedList.head
                self.LinkedList.head = node.next
        return node.value
    def peek(self):
        if self.isEmpty():
            return "The Queue is empty."
        else:
            return self.LinkedList.head.value
    def delete(self):
        self.LinkedList.head == None
        self.LinkedList.tail == None
    

queue = Queue()
print(queue.isEmpty()) # True
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.isEmpty()) # False
print(queue) # 1 2 3 4 5
print(queue.LinkedList.head.value) # 1
print(queue.LinkedList.tail.value) # 5
print(queue.dequeue()) # 1
print(queue.LinkedList.head.value) # 2
print(queue) # 2 3 4 5
print(queue.peek()) # 2
