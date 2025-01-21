# stack is a Data Structure that follows the LIFO (Last In First Out) principle.
# Stack can be implemented using List, Linked List in python.

# Stack using List without size limit.
class Stack:
    def __init__(self):
        self.list = []
    
    # def __str__(self):
    #     values = [str(x) for x in reversed(self.list)]
    #     return '\n'.join(values)

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    # isEmpty() function
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "The element is Successfully added."
    
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack."
        else:
            elem = self.list.pop()
            return f"The element '{elem}' is Successfully removed"
    
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack."
        else:
            return self.list[-1]
    
    def delete(self):
        self.list = None


# creating custom stack
customStack = Stack()
# print(customStack.isEmpty())

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)
print(customStack)
print(customStack.pop())
# print(customStack.isEmpty())
print(customStack)
print(f'Peek : {customStack.peek()}')
