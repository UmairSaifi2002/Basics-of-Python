class BinaryTree:
    def __init__(self, max_size):
        """
        Initialize a binary tree using a list.
        
        :param max_size: Maximum number of nodes the tree can hold.
        """
        self.tree = [None] * max_size  # List to store the tree nodes
        self.last_used_index = 0  # Start indexing from 1 (root at index 1)
        self.max_size = max_size  # Maximum capacity of the tree

    def insert(self, value):
        """
        Insert a new value into the binary tree.
        
        :param value: The value to insert.
        :return: A message indicating success or failure.
        """
        if self.last_used_index + 1 >= self.max_size:
            return "Binary Tree is full. Cannot insert more nodes."
        
        self.last_used_index += 1
        self.tree[self.last_used_index] = value
        return f"Value '{value}' successfully inserted."

    def search(self, target):
        """
        Search for a value in the binary tree.
        
        :param target: The value to search for.
        :return: A message indicating whether the value was found and its index.
        """
        if self.last_used_index == 0:
            return "Binary Tree is empty."
        
        for index in range(1, self.last_used_index + 1):
            if self.tree[index] == target:
                return f"Value '{target}' found at index {index}."
        
        return f"Value '{target}' not found in the tree."

    def pre_order_traversal(self, index):
        """
        Perform pre-order traversal (Root -> Left -> Right) starting from the given index.
        
        :param index: The starting index for traversal.
        """
        if index > self.last_used_index:
            return
        
        print(self.tree[index], end=', ')  # Visit the root
        self.pre_order_traversal(index * 2)  # Traverse the left subtree
        self.pre_order_traversal(index * 2 + 1)  # Traverse the right subtree

    def in_order_traversal(self, index):
        """
        Perform in-order traversal (Left -> Root -> Right) starting from the given index.
        
        :param index: The starting index for traversal.
        """
        if index > self.last_used_index:
            return
        
        self.in_order_traversal(index * 2)  # Traverse the left subtree
        print(self.tree[index], end=', ')  # Visit the root
        self.in_order_traversal(index * 2 + 1)  # Traverse the right subtree

    def post_order_traversal(self, index):
        """
        Perform post-order traversal (Left -> Right -> Root) starting from the given index.
        
        :param index: The starting index for traversal.
        """
        if index > self.last_used_index:
            return
        
        self.post_order_traversal(index * 2)  # Traverse the left subtree
        self.post_order_traversal(index * 2 + 1)  # Traverse the right subtree
        print(self.tree[index], end=', ')  # Visit the root

    def level_order_traversal(self):
        """
        Perform level-order traversal (breadth-first traversal) of the binary tree.
        """
        if self.last_used_index == 0:
            return "Binary Tree is empty."
        
        for index in range(1, self.last_used_index + 1):
            if self.tree[index] is not None:
                print(self.tree[index], end=', ')

    def delete_node(self, value):
        """
        Delete a node with the given value from the binary tree.
        
        :param value: The value of the node to delete.
        :return: A message indicating success or failure.
        """
        if self.last_used_index == 0:
            return "Binary Tree is empty."
        
        for index in range(1, self.last_used_index + 1):
            if self.tree[index] == value:
                # Replace the node with the last node in the tree
                self.tree[index] = self.tree[self.last_used_index]
                self.tree[self.last_used_index] = None
                self.last_used_index -= 1
                return f"Value '{value}' successfully deleted."
        
        return f"Value '{value}' not found in the tree."

    def delete_tree(self):
        """
        Delete the entire binary tree.
        
        :return: A message indicating success.
        """
        self.tree = [None] * self.max_size
        self.last_used_index = 0
        return "Binary Tree successfully deleted."


# Example Usage
if __name__ == "__main__":
    # Create a binary tree with a maximum size of 10
    tree = BinaryTree(10)

    # Insert values into the tree
    print(tree.insert(1))  # Insert 1
    print(tree.insert(2))  # Insert 2
    print(tree.insert(3))  # Insert 3
    print(tree.insert(4))  # Insert 4
    print(tree.insert(5))  # Insert 5
    print(tree.insert(6))  # Insert 6

    # Display the tree structure
    print("Tree List:", tree.tree)

    # Search for a value
    print(tree.search(4))  # Search for 4

    # Perform traversals
    print("Pre-Order Traversal :- ", end=' ')
    tree.pre_order_traversal(1)
    print()

    print("In-Order Traversal :- ", end=' ')
    tree.in_order_traversal(1)
    print()

    print("Post-Order Traversal :- ", end=' ')
    tree.post_order_traversal(1)
    print()

    print("Level-Order Traversal :- ", end=' ')
    tree.level_order_traversal()
    print()

    # Delete a node
    print(tree.delete_node(3))  # Delete node with value 3

    # Perform level-order traversal after deletion
    print("Level-Order Traversal after deletion :- ", end=' ')
    tree.level_order_traversal()
    print()

    # Delete the entire tree
    print(tree.delete_tree())