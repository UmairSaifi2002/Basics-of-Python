class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self, value):  
        self.list.append(value)
        return 'The element is inserted at the end of list.'

    def dequeue(self):
        if self.isEmpty():
            return 'The list is empty.'
        else:
            return self.list.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return 'The Queue is empty.'
        else:
            return self.list[0]
    
    def delete(self):
        self.list = None    


queue = Queue()
print(queue.isEmpty()) # True
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.isEmpty()) # False
print(queue) # 1 2 3 4 5 6
print(queue.dequeue()) # 1
print(queue) # 2 3 4 5 6
print(queue.peek()) # 2
queue.delete()
print(queue.isEmpty()) # True


