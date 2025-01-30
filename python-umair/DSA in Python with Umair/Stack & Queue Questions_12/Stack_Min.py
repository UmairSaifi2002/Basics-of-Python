# Question 2 :- Stack Min
# How would you design a Stack which, in addition to push and pop, has a function min which return the minimum element?
# push, pop, and min should be operate in O(1)

# so this can be done if we implement the stack using linkedlist

# let's get start


class Node:
    def __init__(self, value):
        """
        A class representing a single node in the linked list.

        Parameters:
            value (int): The value stored in the node.
        """
        self.value = value  # The value of the node
        self.next = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        """
        A class representing a linked list for stack implementation.
        """
        self.head = None  # Pointer to the top of the stack
        self.min_node = None  # Pointer to the node storing the minimum value


class Stack:
    def __init__(self):
        """
        A stack implemented using a linked list with O(1) operations for push, pop, and min.
        """
        self.linked_list = LinkedList()

    def __str__(self):
        """
        String representation of the stack for debugging or printing.

        Returns:
            str: A string of all elements in the stack separated by spaces.
        """
        values = []
        current = self.linked_list.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' '.join(values)

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.linked_list.head is None

    def get_min(self):
        """
        Get the minimum value in the stack.

        Returns:
            int/str: The minimum value in the stack or a message if the stack is empty.
        """
        if self.linked_list.min_node is None:
            return "Stack is empty"
        return self.linked_list.min_node.value

    def push(self, value):
        """
        Push a value onto the stack.

        Parameters:
            value (int): The value to push onto the stack.
        """
        # Create a new node for the value
        new_node = Node(value)

        # Update the minimum value node
        if self.linked_list.min_node is None or value < self.linked_list.min_node.value:
            # Store the current minimum node
            min_node = Node(value)
            min_node.next = self.linked_list.min_node
            self.linked_list.min_node = min_node

        # Add the new node to the top of the stack
        new_node.next = self.linked_list.head
        self.linked_list.head = new_node

    def pop(self):
        """
        Remove and return the top value from the stack.

        Returns:
            int/str: The value popped from the stack or a message if the stack is empty.
        """
        if self.is_empty():
            return "Stack is empty"
        
        # Remove the top node and retrieve its value
        popped_value = self.linked_list.head.value
        self.linked_list.head = self.linked_list.head.next

        # Update the minimum node if necessary
        if self.linked_list.min_node and popped_value == self.linked_list.min_node.value:
            self.linked_list.min_node = self.linked_list.min_node.next

        return popped_value


# Example Usage
stack = Stack()

# Push values onto the stack
stack.push(10)
stack.push(20)
stack.push(5)
stack.push(30)
stack.push(3)

# Print the stack's
print("Stack:", stack)

# Get the minimum value
print("Minimum value:", stack.get_min())

# Pop values and print the stack
print("Popped value:", stack.pop())
print("Stack after popping:", stack)
print("Minimum value after popping:", stack.get_min())

        


    

    
