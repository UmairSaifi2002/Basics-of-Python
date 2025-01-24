# circular Queue is called a Queue having Fixed Size.
class Queue:
    def __init__(self, maxSize):
        self.list = maxSize*[None] # Creating an empty list
        self.maxSize = maxSize
        self.start = -1 # start pointer is pointing at the first element
        self.top = -1 # top pointer is pointing at the last element
    
    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    # def isFull(self):
    #     # we have two conditions to declare that Queue is full
    #     if self.top + 1 == self.start:
    #         return True
    #     elif self.start == 0 and self.top + 1 == self.maxSize:
    #         return True
    #     else:
    #         return False
    
    def isFull(self):
        # Calculate the next position after 'top'
        # (self.top + 1) gives the next index position where the new element would go if there is space.
        next_position = (self.top + 1) % self.maxSize  # The modulo ensures the circular behavior.        
        # If the next position after 'top' is equal to 'start', it means the queue is full.
        # This is because when the next position after 'top' matches 'start', it would overwrite
        # the start of the queue, which means there is no more room for new elements.
        return next_position == self.start  # If True, queue is full; else, it is not full.
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    # By me
    # def enqueue(self, value):
    #     if self.isFull():  # If the queue is full
    #         return 'The Queue is Full.'
    #     else:
    #         # Update pointers for the first element
    #         if self.isEmpty():
    #             self.start = 0

    #         # Move the rear pointer circularly
    #         self.top = (self.top + 1) % self.maxSize
    #         self.list[self.top] = value  # Add the element
    #         return f'Inserted {value} into the Queue.'


    # By Sir
    def enqueue(self,value):
        if self.isFull():
            return 'The Queue is Full.'
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value
            return 'The element is inserted at the end of the Queue.'   
    
    # By Umair
    def dequeue(self):
        # Step 1: Check if the queue is empty
        if self.isEmpty():  
            return 'The Queue is Empty.'  # If the queue is empty, there is nothing to remove.    
        else:
            # Step 2: Store the value at the front of the queue
            val = self.list[self.start]  # The element to be removed is at the 'start' position.
            start = self.start  # Temporarily store the current 'start' index for later use.

            # Step 3: Handle the case where the queue becomes empty after removing this element
            if self.start == self.top:  
                # If 'start' equals 'top', it means there was only one element in the queue.
                # After removing it, the queue becomes empty, so reset both pointers.
                self.start = -1
                self.top = -1

            # Step 4: Handle the case where 'start' reaches the end of the circular queue
            elif self.start + 1 == self.maxSize:  
                # If 'start' is at the last index of the queue (`maxSize - 1`), 
                # move 'start' back to the beginning of the queue (index 0).
                self.start = 0

            # Step 5: Normal case - simply move 'start' to the next position
            else:  
                # Increment 'start' to point to the next element in the queue.
                self.start += 1

            # Step 6: Clear the removed element from the queue
            self.list[start] = None  # Set the position where the element was removed to `None`.

            # Step 7: Return the removed value
            return val  # Return the element that was dequeued.
    
    def peek(self):
        # Step 1: Check if the queue is empty
        if self.isEmpty():  
            return 'The Queue is Empty.'  # If the queue is empty.    
        else:
            return self.list[self.start]
    
    def delete(self):
        self.list = self.maxSize*[None]
        self.top = -1
        self.start = -1


queue = Queue(5)
print(queue.isFull()) # False 
print(queue.isEmpty()) # True
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue) # 1 2 3 4 5
print(queue.isFull()) # True
print(queue.isEmpty()) # False
print(queue.dequeue())
print(queue)
