# The MultiStack class enables the implementation of three stacks within a single list, 
# often referred to as the "three-in-one" problem in data structures.

# Question 1 :- Three in One
# Describe how we use one Single python list to implement three stacks

class MultiStack:
    def __init__(self, max_stack_size):
        """
        Initialize a class to manage three stacks in one list.

        Parameters:
            max_stack_size (int): The maximum size of each stack.
        """
        self.num_of_stacks = 3  # Total number of stacks
        self.stack_data = [0] * (self.num_of_stacks * max_stack_size)  # List to hold all stack elements
        self.stack_sizes = [0] * self.num_of_stacks  # Tracks the current number of elements in each stack
        self.max_stack_size = max_stack_size  # Maximum size allowed for each stack

    def is_full(self, stack_num):
        """
        Check if the specified stack is full.

        Parameters:
            stack_num (int): The index of the stack (0, 1, or 2).

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return self.stack_sizes[stack_num] == self.max_stack_size

    def is_empty(self, stack_num):
        """
        Check if the specified stack is empty.

        Parameters:
            stack_num (int): The index of the stack (0, 1, or 2).

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.stack_sizes[stack_num] == 0

    def get_top_index(self, stack_num):
        """
        Get the index of the top element of the specified stack in the shared list.

        Parameters:
            stack_num (int): The index of the stack (0, 1, or 2).

        Returns:
            int: The index of the top element in the shared list.
        """
        start_index = stack_num * self.max_stack_size  # Starting index for the given stack
        return start_index + self.stack_sizes[stack_num] - 1  # Calculate top index based on stack size

    def push(self, stack_num, value):
        """
        Add an element to the top of the specified stack.

        Parameters:
            stack_num (int): The index of the stack (0, 1, or 2).
            value (int): The value to add to the stack.

        Returns:
            str: A message if the stack is full, otherwise None.
        """
        if self.is_full(stack_num):
            return "Stack is Full"
        else:
            # Increase the size of the stack and add the value at the calculated top index
            self.stack_sizes[stack_num] += 1
            top_index = self.get_top_index(stack_num)
            self.stack_data[top_index] = value

    def pop(self, stack_num):
        """
        Remove and return the top element of the specified stack.

        Parameters:
            stack_num (int): The index of the stack (0, 1, or 2).

        Returns:
            int/str: The value removed from the stack, or a message if the stack is empty.
        """
        if self.is_empty(stack_num):
            return "Stack is Empty"
        else:
            # Get the top index, retrieve the value, and remove it by resetting to 0
            top_index = self.get_top_index(stack_num)
            value = self.stack_data[top_index]
            self.stack_data[top_index] = 0
            self.stack_sizes[stack_num] -= 1  # Decrease the size of the stack
            return value

    def peek(self, stack_num):
        """
        Get the top element of the specified stack without removing it.

        Parameters:
            stack_num (int): The index of the stack (0, 1, or 2).

        Returns:
            int/str: The value at the top of the stack, or a message if the stack is empty.
        """
        if self.is_empty(stack_num):
            return "Stack is Empty"
        else:
            # Get the value at the top index without modifying the stack
            top_index = self.get_top_index(stack_num)
            return self.stack_data[top_index]


# Example Usage
stack = MultiStack(6)  # Create a MultiStack with each stack having a maximum size of 6

# Check if stacks are empty
print(stack.is_empty(0))  # True
print(stack.is_empty(1))  # True
print(stack.is_empty(2))  # True

# Check if stacks are full
print(stack.is_full(0))  # False
print(stack.is_full(1))  # False
print(stack.is_full(2))  # False

# Push elements into the stacks
stack.push(0, 1)
stack.push(0, 2)
stack.push(0, 3)
stack.push(0, 4)
print(stack.peek(0))  # 4 (Top element of Stack 0)

stack.push(1, 10)
stack.push(1, 20)
stack.push(1, 30)
stack.push(1, 40)
print(stack.peek(1))  # 40 (Top element of Stack 1)

stack.push(2, 100)
stack.push(2, 200)
stack.push(2, 300)
stack.push(2, 400)
print(stack.peek(2))  # 400 (Top element of Stack 2)

# Pop elements from the stacks
print(stack.pop(0))  # 4
print(stack.pop(1))  # 40
print(stack.pop(2))  # 400
