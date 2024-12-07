# Creating a Node element class
class Node:
    def __init__(self, value): # it is a Constructor as we have in java it is also a dunder method in python
        self.value = value # here we set a value to the node
        self.next = None # here we make point to None initially

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Insert at the Beginning
    def insertAtBeginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insert at the last
    def insertAtLast(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.tail = new_node
    
    # print the LinkedList
    def display(self):
        curr = self.head
        while curr:
            print(f"{curr.value} -> ",end='')
            curr = curr.next
        print('None')

ll = LinkedList()
ll.insertAtBeginning(2)
ll.insertAtBeginning(1)
ll.insertAtBeginning(0)
ll.insertAtLast(3)
ll.insertAtLast(4)
ll.insertAtLast(5)
ll.display()