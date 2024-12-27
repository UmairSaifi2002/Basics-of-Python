# Interview Question on Linked List
from random import randint

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next
    
    def __str__(self):
        value = [str(x.value) for x in self]
        return ' -> '.join(value)
    
    def __len__(self):
        result = 0
        currNode = self.head
        while currNode:
            result += 1
            currNode = currNode.next
        return result

    def add(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
            self.length += 1
        
    def generate(self, n, miniValue, maxValue):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(miniValue, maxValue))
        return self

    def remove_duplicates(ll):
        if ll.head is None or ll.head.next is None:
            # Empty list or single-node list: no duplicates
            return ll.head        
        # Set to track unique values
        seen_values = set()        
        # Initialize pointers
        current = ll.head
        seen_values.add(current.value)  # Add the first node's value to the set
        while current.next:
            if current.next.value in seen_values:
                # Duplicate found; skip the node
                current.next = current.next.next
            else:
                # Add the value to the set and move forward
                seen_values.add(current.next.value)
                current = current.next
        return ll.head  # Return the head of the modified linked list

    # in this function we will find the nth node from the last
    # we assume that this is a singly linked list
    # with unknown length
    def nthfromLast(self, n):
        p = self.head
        q = self.head
        for i in range(n):
            if q is None:
                return None
            q = q.next
        while q is not None:
            p = p.next
            q = q.next
        return p
    
    # here we will partion the linkedlist around a given value
    # only for non circular linkedlist
    def partition(self,value):
        currNode = self.head
        self.tail = currNode
        nextNode = currNode.next
        currNode.next = None
        while nextNode:
            temp = nextNode.next
            if nextNode.value < value:
                nextNode.next = self.head
                self.head = nextNode
            else:
                self.tail.next = nextNode
                self.tail = nextNode
            nextNode = temp

LL = LinkedList()
LL.generate(10, 0, 30)
print(LL) # 10 -> 20 -> 30 -> 20 -> 10 -> 20 -> 10 -> 10 -> 10 -> 20
print(len(LL)) # 10

# LL.remove_duplicates()
# print(LL) 

LL.partition(15)
print(LL)
