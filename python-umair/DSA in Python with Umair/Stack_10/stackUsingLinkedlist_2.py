# Here We are trying to create a Stack with LinkedList.
# Node class
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

#  Stack class
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    # here we create a __str__ method which uses the __iter__ method
    # and return the value of the node in the stack
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return ' '.join(values)
    
    # this str method works all
    # means if we print the stack which is created by the linkedlist 
    # so we do not need the __iter__ method in the LinkedList class
    def __str__(self):
        value = []
        n = self.LinkedList.head
        # print(n.value)
        while(n):
            value.append(str(n.value))
            n = n.next
        # print(value)
        return ' '.join(value)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        node = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = node
        else:
            node.next = self.LinkedList.head
            self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            node = self.LinkedList.head
            self.LinkedList.head = self.LinkedList.head.next
            node.next = None
            return node.value
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element is in the Stack."
        else:
            return self.LinkedList.head.value
    
    def delete(self):
        self.LinkedList.head = None
        return "The Stack is Successfully deleted."

stack = Stack() # crreating a custom Stack using LinkedList
print(stack.isEmpty()) # True
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5) 
stack.push(6) 
print(stack.isEmpty()) # False
print(stack) # 6 5 4 3 2 1
print(stack.pop()) # 6
print(stack) # 5 4 3 2 1
print(stack.peek()) # 5
print(stack) # 5 4 3 2 1
print(stack.delete()) # The Stack is Successfully deleted.
print(stack) # 
print(stack.isEmpty()) # True
