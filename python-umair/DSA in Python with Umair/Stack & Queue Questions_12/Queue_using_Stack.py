# Question 4 :- Queue via Stack
# Implement Queue class which implement a queue uisng two stacks.

class Queue:
    def __init__(self):
        """
        Initialize a queue using two stacks (lists).
        - `input_stack` is used to hold incoming items.
        - `temp_stack` is used for reversing the order during dequeue operations.
        """
        self.input_stack = []  # Stack to hold incoming elements
        self.temp_stack = []  # Stack to temporarily hold elements during dequeue

    def __str__(self):
        """
        String representation of the queue.
        """
        # Join all elements in the input_stack to form a string
        elements = [str(item) for item in self.input_stack]
        return ' '.join(elements)

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Parameters:
        - item: The item to be added to the queue.
        """
        self.input_stack.append(item)

    def dequeue(self):
        """
        Remove and return the front item of the queue.
        This is done by temporarily moving elements to a secondary stack to reverse the order.
        
        Returns:
        - The dequeued item.
        """
        # Move all elements from input_stack to temp_stack to reverse order
        while self.input_stack:
            element = self.input_stack.pop()
            self.temp_stack.append(element)

        # The last item in temp_stack is the front of the queue
        dequeued_item = self.temp_stack.pop()

        # Move the elements back from temp_stack to input_stack to restore the original order
        while self.temp_stack:
            element = self.temp_stack.pop()
            self.input_stack.append(element)

        return dequeued_item


# Example Usage
queue = Queue()

# Add items to the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print("Queue after enqueuing items:", queue)  # Output: Queue after enqueuing items: 1 2 3 4 5 6

# Remove and print items from the queue
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 1
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 2
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 3

print("Queue after dequeuing items:", queue)  # Output: Queue after dequeuing items: 4 5 6
