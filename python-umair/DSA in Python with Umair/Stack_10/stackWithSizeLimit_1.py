# Here we gonna create a stack using list which has a size limit.
class Stack:
    def __init__(self, maxsize):
        self.list = []
        self.lenght = maxsize

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.lenght:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "The Stack is Full!"
        else:
            self.list.append(value)
            return "The element is Successfully added."
    
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack."
        else:
            elem = self.list.pop()
            return f"The element {elem} is Successfully removed."
    
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack."
        else:
            return self.list[-1]

    def delete(self):
        self.list = None
        return "The stack is Successfully deleted."

# now running our code to check the implementation of stack with size limit.
customstack = Stack(6)
print(customstack.isEmpty()) # True
print(customstack.isFull()) # False
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
print(customstack) # 1 2 3 4
print(customstack.isEmpty()) # False 
print(customstack.isFull()) # False
customstack.push(5)
customstack.push(6)
customstack.push(7)
print(customstack) # 1 2 3 4 5 6
print(customstack.isFull()) # True
print(customstack.pop()) # The element 6 is Successfully removed.
print(customstack) # 1 2 3 4 5
print(customstack.peek()) # 5

