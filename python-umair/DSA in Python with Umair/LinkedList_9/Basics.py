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

    # Prepand method -> O(1)
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

    # append method -> O(1)
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

    # insert method -> O(n)
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
    # pop_first method  -> O(1)
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
    # pop method -> O(n)
    def POP(self):
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
    # remove method -> O(n)
    def remove(self, index):
        '''
        Pop the element in between the linked list
        '''
        if self.length is 0:
            return None
        if self.length is 1:
            curr = self.head
            self.head = None
            self.tail = None
            return curr
        if index >= self.length:
            return "ERROR: Index is Out of Bound"
        else:
            curr = self.head
            # print(curr.value)
            i = 1
            while i < index-1:
                curr = curr.next
                i +=1
            prev = curr
            popped = curr.next
            prev.next = popped.next
            popped.next = None
            return popped
    
    # delete all the nodes
    # delete method -> O(1)
    def delete(self):
        self.head = None
        self.tail = None
        return None
    
    # Search an element in a linkedlist
    # search method -> O(n)
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
    
    # get_Method -> O(n)
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # set_Method -> O(n)
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

    # Pints the LinkedList  -> O(n)
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

    # Prints the LinkedLists using dunder method  -> O(n)   
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
    
    # # Reverse a LinkedList
    def Reverse(self):
        if self.length is 0: # Check if the linked list is empty
            return "Error: Linked List is Empty"
        elif self.length is 1: # Check if the linked list contains only one node
            return "Already Reversed"
        else:
            prev = None
            curr = self.head
            Next = curr.next # Initialize the 'Next' variable with the next node
            # Swap the head and tail pointers
            self.head, self.tail = self.tail, self.head
            while curr is not None:
                curr.next = prev  # Reverse the 'next' pointer of the current node
                prev = curr  # Move the 'prev' pointer to the current node
    
                # Update 'Next' before moving 'curr' to avoid NoneType errors
                curr = Next  # Move the 'curr' pointer to the next node
                if Next is not None:
                    Next = Next.next  # Update 'Next' to the next node
    
    # finding out the middle of the linkedlist
    def Middle_of_LinkedList(self):
        '''
        Check the linkedlist for palindrome
        '''
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # remove Duplicates
    # By me
    # def remove_duplicate(self):
    #     ls = []
    #     temp = self.head
    #     while temp is not None:
    #         a = temp.value
    #         if a not in ls:
    #             ls.append(a)
    #         temp = temp.next
    #     # print(ls)
    #     self.head = None
    #     self.tail = None
    #     for i in range(len(ls)):
    #         linked_list.insert_at_end(ls[i])

    # By sir
    def remove_duplicate(self):
        if self.head is None:
            return "Nothing is here"
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

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
    linked_list.POP()
    print(linked_list)

    # pop the element
    linked_list.remove(5)
    print(linked_list)

    # Reverse a linked list
    # linked_list.Reverse()
    # print(linked_list)

    linked_list.insert_at_beginning(1)
    linked_list.insert_at_end(1)
    print(linked_list)
    linked_list.remove_duplicate()
    print(linked_list)
