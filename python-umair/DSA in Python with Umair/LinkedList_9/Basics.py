# Define a Node class to represent each element in the LinkedList
class Node:
    def __init__(self, value):
        """
        Initialize a Node with a value and a pointer to the next node.
        Initially, the 'next' pointer is set to None.
        """
        self.value = value
        self.next = None


# Define the LinkedList class
class LinkedList:
    def __init__(self):
        """
        Initialize an empty LinkedList with a head, tail, and length attribute.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def insert_at_beginning(self, value):
        """
        Insert a new node at the beginning of the LinkedList.
        """
        new_node = Node(value)
        new_node.next = self.head  # Point the new node's 'next' to the current head
        self.head = new_node  # Update the head to the new node

        # If the list was empty, update the tail as well
        if self.tail is None:
            self.tail = new_node

        self.length += 1

    def insert_at_end(self, value):
        """
        Insert a new node at the end of the LinkedList.
        """
        new_node = Node(value)

        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:  # If the list is not empty
            self.tail.next = new_node  # Point the current tail's 'next' to the new node
            self.tail = new_node  # Update the tail to the new node

        self.length += 1

    def insert_at_position(self, value, position):
        """
        Insert a new node at a specified position in the LinkedList.
        """
        if position < 0 or position > self.length:
            return "Error: Position out of bounds."

        if position == 0:  # Insert at the beginning
            return self.insert_at_beginning(value)

        if position == self.length:  # Insert at the end
            return self.insert_at_end(value)

        # Insert in between
        new_node = Node(value)
        current = self.head
        for _ in range(position - 1):  # Traverse to the node before the position
            current = current.next

        new_node.next = current.next  # Point the new node's 'next' to the next node
        current.next = new_node  # Update the current node's 'next' to the new node

        self.length += 1
    
    # pop the first element from the linkedlist
    def popFirst(self):
        '''
        PoP first element from the linkedlist
        '''
        if self.length == 0:
            return None
        curr = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return curr
        elif self.length > 1:
            self.head = curr.next
            curr.next = None
            self.length -= 1
        return curr
    
    # pop last element from the linkedlist
    def popLast(self):
        '''
        POP last element from the linkedlist
        '''
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        popped = curr.next
        curr.next = None
        self.tail = curr
        self.length -= 1
        return popped
    
    # pop the element in between the linkedlist
    def pop(self, index):
        '''
        Pop the element in between the linked list
        '''
        curr = self.head
        for _ in range(index-2):
            curr = curr.next
        popped = curr
        curr.next = curr.next.next
        popped.next = None
        self.length -= 1
        return popped
    
    # Search an element in a linkedlist
    def search(self,value):
        '''
        Searching an element in a Linkedlist
        '''
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    # get_Method 
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # set_Method
    def set_value(self, index, value):
        if index == 0:
            self.head.value = value
        elif index == self.length-1:
            self.tail.value = value
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.value = value

    # Pints the LinkedList
    def display(self):
        """
        Print all elements in the LinkedList.
        """
        if not self.head:  # Check if the list is empty
            print("The LinkedList is empty.")
            return

        current = self.head
        while current:
            print(f"{current.value} -> ", end="")
            current = current.next
        print("None")

    # Prints the LinkedLists using dunder method
    def __str__(self):
        """
        Override the default string representation of the LinkedList for easier debugging.
        """
        if not self.head:  # Check if the list is empty
            return "The LinkedList is empty."

        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next

        return " -> ".join(result) + " -> None"


# Demonstrating LinkedList functionality
if __name__ == "__main__":
    # Create an instance of LinkedList
    linked_list = LinkedList()

    # Insert elements at the beginning
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(1)

    # Insert elements at the end
    linked_list.insert_at_end(15)
    linked_list.insert_at_end(20)

    # Display the LinkedList
    print("Initial LinkedList:")
    linked_list.display()

    # Insert elements at specific positions
    linked_list.insert_at_position(7, 2)  # Insert 7 at position 2
    linked_list.insert_at_position(25, linked_list.length)  # Insert 25 at the end
    linked_list.insert_at_position(0, 0)  # Insert 0 at the beginning

    # Display the LinkedList after insertions
    print("\nLinkedList after insertions:")
    print(linked_list)  # Using the __str__ method

    # Print the length of the LinkedList
    print(f"\nLength of LinkedList: {linked_list.length}")

    # Searching the element in the LinkedList
    print(linked_list.search(25))

    # Set the value of particular node
    linked_list.set_value(0,40)
    linked_list.set_value(linked_list.length-1,400)
    linked_list.set_value(5,4000)
    print(linked_list)

    # popping the first element from the linkedlist
    linked_list.popFirst()
    print(linked_list)

    # popping the last element from the linkedlist
    linked_list.popLast()
    print(linked_list)

    # pop the element
    linked_list.pop(5)
    print(linked_list)
