class Node:
    def __init__(self, data):
        self.data = data  # Store the value of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list
        self.length = 0   # Track the number of nodes in the list

    def __str__(self):
        # Return the string representation of the list
        temp = self.head
        result = 'None <- '
        while temp:
            result += str(temp.data)
            if temp.next:
                result += ' <-> '
            temp = temp.next
        result += ' -> None'
        return result

    def append(self, data):
        # Add a node to the end of the list
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
        else:  # Otherwise, attach to the end
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def preppend(self, data):
        # Add a node to the beginning of the list
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = self.tail = new_node
        else:  # Otherwise, attach to the front
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        # Traverse and print the list from head to tail
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def ReverseTreverse(self):
        # Traverse and print the list from tail to head
        temp = self.tail
        while temp:
            print(temp.data, end=' ')
            temp = temp.prev
        print()

    def search(self, target):
        # Search for a value in the list
        temp = self.head
        while temp:
            if temp.data == target:
                return True
            temp = temp.next
        return False

    def Get(self, index):
        # Retrieve the node at a specific index
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:  # Traverse from head
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:  # Traverse from tail
            curr = self.tail
            for _ in range(self.length - 1, index, -1):
                curr = curr.prev
        return curr

    def insert(self, index, data):
        # Insert a node at a specific index
        if index < 0 or index > self.length:
            print('Index Out of Bounds')
            return
        if index == 0:
            self.preppend(data)
        elif index == self.length:
            self.append(data)
        else:
            new_node = Node(data)
            prev_node = self.Get(index - 1)
            next_node = prev_node.next
            new_node.prev = prev_node
            new_node.next = next_node
            prev_node.next = new_node
            next_node.prev = new_node
            self.length += 1

    def popFirst(self):
        # Remove and return the first node
        if not self.head:  # Empty list
            return None
        popped_node = self.head
        if self.length == 1:  # Single-node list
            self.head = self.tail = None
        else:
            self.head = popped_node.next
            self.head.prev = None
        popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        # Remove and return the last node
        if not self.head:  # Empty list
            return None
        popped_node = self.tail
        if self.length == 1:  # Single-node list
            self.head = self.tail = None
        else:
            self.tail = popped_node.prev
            self.tail.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        # Remove a node at a specific index
        if not self.head:  # Empty list
            return None
        if index < 0 or index >= self.length:
            print('Index Out of Bounds')
            return
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        node_to_remove = self.Get(index)
        prev_node = node_to_remove.prev
        next_node = node_to_remove.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node_to_remove.next = node_to_remove.prev = None
        self.length -= 1
        return node_to_remove


# Testing the DoublyLinkedList class
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print(dll)  # None <- 1 <-> 2 <-> 3 <-> 4 <-> 5 -> None

dll.preppend(0)
dll.preppend(-1)
print(dll)  # None <- -1 <-> 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 -> None

dll.traverse()  # -1 0 1 2 3 4 5
dll.ReverseTreverse()  # 5 4 3 2 1 0 -1
print(dll.search(4))  # True
print(dll.search(7))  # False

dll.insert(3, 100)
print(dll)  # None <- -1 <-> 0 <-> 1 <-> 100 <-> 2 <-> 3 <-> 4 <-> 5 -> None

dll.popFirst()
print(dll)  # None <- 0 <-> 1 <-> 100 <-> 2 <-> 3 <-> 4 <-> 5 -> None

dll.pop()
print(dll)  # None <- 0 <-> 1 <-> 100 <-> 2 <-> 3 <-> 4 -> None

dll.remove(3)
print(dll)  # None <- 0 <-> 1 <-> 100 <-> 2 <-> 4 -> None
dll.remove(2)
print(dll)