class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp = self.head
        result = 'None <- '
        while temp is not None:
            result += str(temp.data)
            if temp.next is not None:
                result += ' <-> '
            temp = temp.next
        result += ' -> None'
        return result
    
    def append(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        self.length += 1
    
    def preppend(self,data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        self.length += 1
    
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=' ')
            temp = temp.next
    
    def ReverseTreverse(self):
        temp = self.tail
        while temp is not None:
            print(temp.data,end=' ')
            temp = temp.prev
    
    def search(self,target):
        temp = self.head
        while temp is not None:
            if target == temp.data:
                return True
            temp = temp.next
        return False
    
    def Get(self, index):
        # Validate the index
        if index < 0 or index >= self.length:
            return None
        # Optimized traversal
        if index < self.length // 2:
            # Traverse from the head
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            # Traverse from the tail
            curr = self.tail
            for _ in range(self.length - 1, index, -1):
                curr = curr.prev
        return curr
    
    def SetValue(self,index,data):
        node = self.Get(index)
        if node:
            node.data = data
            return True
        return False
    
    def insert(self, index, data):
        if index < 0 or index > self.length:
            print('Index Out of Bounds')
            return
        new_node = Node(data)
        if index == 0:
            self.preppend(data)
            return 
        if index == self.length:
            self.append(data)
            return
        temp_node = self.Get(index-1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next = new_node
        temp_node.next.prev = new_node
    
    def popFirst(self):
        if self.head is None:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        # Case 1: Empty list
        if self.head is None:
            return None
        # Save the tail node to be removed
        popped_node = self.tail
        # Case 2: Single-node list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Case 3: More than one node
        else:
            self.tail = popped_node.prev  # Update tail to the previous node
            self.tail.next = None         # Disconnect the last node
            popped_node.prev = None       # Clean up the popped node's references
        # Update the length of the list
        self.length -= 1
        # Return the removed node
        return popped_node

    def remove(self, index):
        # Case 1: Empty list
        if self.head is None:
            return None
        # Case 2: Index out of bounds
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        # Case 3: Remove the first node
        if index == 0:
            return self.popFirst()
        # Case 4: Remove the last node
        if index == self.length - 1:
            return self.pop()
        # Case 5: Remove an intermediate node
        popped_node = self.Get(index)  # Get the node at the specified index
        previous_node = popped_node.prev
        next_node = popped_node.next
        # Update pointers to remove the node
        previous_node.next = next_node
        next_node.prev = previous_node
        # Clean up the removed node's references
        popped_node.prev = None
        popped_node.next = None
        # Update the length
        self.length -= 1
        # Return the removed node
        return popped_node


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print(dll) # None <- 1 <-> 2 <-> 3 <-> 4 <-> 5 -> None

dll.preppend(0)
dll.preppend(-1)
print(dll) # None <- -1 <-> 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 -> None

dll.traverse()
print()
dll.ReverseTreverse()
print()
print(dll.search(4))
print(dll.search(7))

print(dll.Get(3).data)
print(dll.Get(2).data)
print(dll.Get(-1))
print(dll.Get(7))

dll.insert(3,100)
print(dll)

print(dll.popFirst().data)
print(dll)
