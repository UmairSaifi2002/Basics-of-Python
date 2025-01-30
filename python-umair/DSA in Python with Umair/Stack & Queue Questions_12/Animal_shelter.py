# Question 5 :- Animal Shelter
# An Animal Shelter, which holds only dogs and cats, operate only in FIFO manner.
# People must adopt either the oldest of all the animal at the shelter
# or they can select whether they would prefer a dog or cat.
# They cannot select which specific animal they woulld like.
# Create a Data Structure to maintain this system and implement operation such as enqueue, dequeue, dequeueDog, dequeueCat

class Queue:
    def __init__(self):
        self.main_list = []
        self.helper_list = []
    
    def __str__(self):
        elem = [str(item) for item in self.main_list]
        return ', '.join(elem)
    
    def enqueue(self, value):
        self.main_list.append(value)
        return 'append SuccessFully.'
    
    def dequeue(self):
        while self.main_list:
            elem = self.main_list.pop()
            self.helper_list.append(elem)
        val = self.helper_list.pop()
        while self.helper_list:
            elem = self.helper_list.pop()
            self.main_list.append(elem)
        return val
    
    def dequeueDog(self):
        self.main_list.remove('Dog')

    def dequeueCat(self):
        self.main_list.remove('Cat')

queue = Queue()
queue.enqueue('Dog')
queue.enqueue('Cat')
queue.enqueue('Dog')
queue.enqueue('Cat')
queue.enqueue('Cat')
queue.enqueue('Cat')
queue.enqueue('Dog')
queue.enqueue('Cat')
print(queue) # Dog, Cat, Dog, Cat, Cat, Cat, Dog, Cat
queue.dequeue()
print(queue) # Cat, Dog, Cat, Cat, Cat, Dog, Cat
queue.dequeueDog()
print(queue) # Cat, Cat, Cat, Cat, Dog, Cat
queue.dequeueCat()
print(queue) # Cat, Cat, Cat, Dog, Cat
