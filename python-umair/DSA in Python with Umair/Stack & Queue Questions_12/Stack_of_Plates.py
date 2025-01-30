# Question 3 :- Stack of Plates
# Imagine a Stack of Plates. If the Stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack
# when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should
# be composed of several stacks and should create a new stack once the previous one exceeds capacity, SetOfStack.push() and SetOfStack.pop()
# should behave identically to a single stack

# Follow Up:
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

class PlateStack:
    def __init__(self, stack_capacity):
        """
        Initialize a PlateStack object with a maximum capacity for each stack.
        
        Parameters:
        - stack_capacity (int): The maximum number of plates allowed in a single stack.
        """
        self.stack_capacity = stack_capacity  # Maximum plates per stack
        self.stacks = []  # List to hold all stacks (a list of lists)

    def __str__(self):
        """
        Return a string representation of all stacks.
        """
        return str(self.stacks)

    def push(self, plate):
        """
        Add a plate to the stack system. If the last stack is full, create a new stack.
        
        Parameters:
        - plate: The plate to add.
        """
        # Check if there is at least one stack and if the last stack has space
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.stack_capacity:
            # Add the plate to the last stack
            self.stacks[-1].append(plate)
        else:
            # Create a new stack (a new list) and add the plate to it
            self.stacks.append([plate])

    def pop(self):
        """
        Remove the top plate from the stack system. If the last stack is empty after removal, delete it.

        Returns:
        - The removed plate, or a message if the stack system is empty.
        """
        if len(self.stacks) == 0:  # No stacks present
            return "No plates to remove"

        # Remove the top plate from the last stack
        top_plate = self.stacks[-1].pop()

        # If the last stack is now empty, remove it from the list of stacks
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return top_plate

    def pop_at(self, stack_index):
        """
        Remove a plate from a specific stack by index.

        Parameters:
        - stack_index (int): The index of the stack to remove a plate from.

        Returns:
        - The removed plate, or a message if the index is invalid or the stack is empty.
        """
        if stack_index < 0 or stack_index >= len(self.stacks):
            return "Invalid stack index"

        # Remove the top plate from the specified stack
        top_plate = self.stacks[stack_index].pop()

        # If the specified stack is now empty, remove it from the list of stacks
        if len(self.stacks[stack_index]) == 0:
            del self.stacks[stack_index]

        return top_plate


plate_stack = PlateStack(stack_capacity=2)

# Add plates
plate_stack.push(1)
plate_stack.push(2)
plate_stack.push(3)
plate_stack.push(4)
plate_stack.push(5)

print("Stacks after pushing:", plate_stack)  # Output: [[1, 2], [3, 4], [5]]

# Remove a plate
plate_stack.pop()
print("Stacks after popping:", plate_stack)  # Output: [[1, 2], [3, 4]]

# Remove a plate from a specific stack
plate_stack.pop_at(0)
print("Stacks after popping at stack 0:", plate_stack)  # Output: [[1], [3, 4]]

