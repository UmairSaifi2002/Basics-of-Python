class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.data)
            if temp.next is self.head:
                break
            result += ' <-> '
            temp = temp.next
        return result
    
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1
    
    def preppend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1
    
    def insert(self, index, data):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.preppend(data)
        elif index == self.length - 1:
            self.append(data)
        else:
            new_node = Node(data)
            temp = self.head
            for _ in range(index):
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
        self.length += 1
    
    def traverse(self): 
        temp = self.head
        while temp is not None:
            print(temp.data,end=' ')
            if temp.next is self.head:
                break
            temp = temp.next
    
    def ReverseTraverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.data,end=' ')
            if temp.prev is self.tail:
                break
            temp = temp.prev
    
    def search(self,index):
        temp = self.head
        while temp is not None:
            if temp.data == index:
                return True
            temp = temp.next
            if temp is self.head: # to escape from the loop
                break
        return False
    
    def Get(self, index):
        # Check if the index is out of bounds or the list is empty
        if index < 0 or index >= self.length or self.head is None:
            return None
        # Optimize traversal based on index position
        if index <= self.length // 2:
            # Traverse from the head
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            # Traverse from the tail
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length or self.head is None:
            return None
        if index == 0:
            self.head.data = value
        elif index == self.length - 1:
            self.tail.data = value
        else:
            self.Get(index).data = value
    
    def pop_first(self):
        if self.head is None:
            return None  # Empty list, nothing to pop
        popped = self.head  # Save the current head node
        if self.length == 1:
            # Case 1: Single-node list
            self.head = None
            self.tail = None
        else:
            # Case 2: Multiple-node list
            self.head = self.head.next  # Update head to the next node
            self.head.prev = None       # Remove reference to the old head
            popped.next = None          # Clean up popped node's next pointer
            self.tail.next = self.head  # Update the tail's next pointer
            self.head.prev = self.tail  # Update the head's prev pointer
        self.length -= 1  # Decrement the length of the list
        return popped
    
    def pop(self):
        if self.head is None:
            return None
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        popped.next = None
        popped.prev = None
        self.length -= 1
        return popped
    
    def remove(self, index):
        temp = self.head
        if index < 0 or index >= self.length or self.length == 0:
            return None
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            for _ in range(index):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None
            self.length -= 1
        return temp
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

cdll = CircularDoublyLinkedList()
# append the elements
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
cdll.append(50)
cdll.append(60)
print(cdll) # 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> 60

# inserting the element
cdll.insert(2, 350)
print(cdll)

# traversing the elements
cdll.traverse() # 10 20 30 350 40 50 60
print()

# rversing the elements
cdll.ReverseTraverse() # 60 50 40 350 30 20 10
print()

# searching the elements
print(cdll.search(20)) # True
print(cdll.search(40)) # True
print(cdll.search(70)) # False

# getting the value of the elements
print(cdll.Get(5).data) # 60

# setting value of the elements
cdll.set_value(0, 100) 
cdll.set_value(2, 300)
cdll.set_value(5, 600)
print(cdll) # 100 <-> 20 <-> 300 <-> 350 <-> 40 <-> 50 <-> 600

# inserting the elements 
cdll.insert(0,0)
cdll.insert(6,7)
print(cdll) # 0 <-> 100 <-> 20 <-> 300 <-> 350 <-> 40 <-> 600 <-> 7 <-> 60

# poping the elements
print(cdll.pop_first().data) # 0
print(cdll.pop().data) # 60
print(cdll) # 100 <-> 20 <-> 300 <-> 350 <-> 40 <-> 600 <-> 7

# removing the element
# print(cdll.remove(2).data) # 300
# print(cdll) # 100 <-> 20 <-> 350 <-> 40 <-> 600 <-> 7
# print(cdll.remove(0).data) # 100
# print(cdll) # 20 <-> 350 <-> 40 <-> 600 <-> 7
# print(cdll.remove(4).data) # 7
# print(cdll) # 20 <-> 350 <-> 40 <-> 600