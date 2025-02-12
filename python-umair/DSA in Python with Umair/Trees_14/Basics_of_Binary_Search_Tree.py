# Now we will Learn about Binary Search Tree
# A Binary Search Tree is a tree-like data structure where each node has:

# - A value (also called a key)
# - A left child node - less than root node
# - A right child node - greater than root node

# Properties
# 1. Ordered: For any node, all elements in its left subtree are less than the node's value, and all elements in its right subtree are greater.
# 2. Unique: No duplicate values are allowed in the tree.
# 3. Binary: Each node has at most two children (left and right).

# importing queue from anoher file
# Importing queue from another file
import sys
queue_folder_path = r"c:\\Users\\umair\\OneDrive\\Desktop\\Programming\\Basics-of-Python\\python-umair\\DSA in Python with Umair\\Queue_11"
sys.path.append(queue_folder_path)

import BasicOfQueue as queue

class TreeNode:
    """Node structure for the BST."""
    def __init__(self, data):
        self.data = data  # Value of the node
        self.leftChild = None  # Left child of the node
        self.rightChild = None  # Right child of the node

class BinarySearchTree:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None  # Root of the BST

    def insertNode(self, nodeValue, currentNode=None):
        """
        Insert a node into the BST.
        If `currentNode` is not provided, it starts from the root.
        """
        if self.root is None:
            # If the tree is empty, create the root node
            self.root = TreeNode(nodeValue)
            return 'The node has been successfully inserted.'

        if currentNode is None:
            # Start from the root if no current node is provided
            currentNode = self.root

        if nodeValue <= currentNode.data:
            # If the value is less than or equal to the current node, go to the left subtree
            if currentNode.leftChild is None:
                # If left child is empty, insert the new node here
                currentNode.leftChild = TreeNode(nodeValue)
            else:
                # Otherwise, recursively insert in the left subtree
                self.insertNode(nodeValue, currentNode.leftChild)
        else:
            # If the value is greater than the current node, go to the right subtree
            if currentNode.rightChild is None:
                # If right child is empty, insert the new node here
                currentNode.rightChild = TreeNode(nodeValue)
            else:
                # Otherwise, recursively insert in the right subtree
                self.insertNode(nodeValue, currentNode.rightChild)

        return 'The node has been successfully inserted.'

    def preOrderTraversal(self, rootNode):
        """
        Perform pre-order traversal (Depth First Search).
        Order: Root -> Left -> Right
        """
        if rootNode is None:
            return
        print(rootNode.data, end=', ')  # Print the root node
        self.preOrderTraversal(rootNode.leftChild)  # Traverse the left subtree
        self.preOrderTraversal(rootNode.rightChild)  # Traverse the right subtree

    def inOrderTraversal(self, rootNode):
        """
        Perform in-order traversal (Depth First Search).
        Order: Left -> Root -> Right
        """
        if rootNode is None:
            return
        self.inOrderTraversal(rootNode.leftChild)  # Traverse the left subtree
        print(rootNode.data, end=', ')  # Print the root node
        self.inOrderTraversal(rootNode.rightChild)  # Traverse the right subtree

    def postOrderTraversal(self, rootNode):
        """
        Perform post-order traversal (Depth First Search).
        Order: Left -> Right -> Root
        """
        if rootNode is None:
            return
        self.postOrderTraversal(rootNode.leftChild)  # Traverse the left subtree
        self.postOrderTraversal(rootNode.rightChild)  # Traverse the right subtree
        print(rootNode.data, end=', ')  # Print the root node

    def levelOrderTraversal(self, rootNode):
        """
        Perform level-order traversal (Breadth First Search).
        Order: Level by level, from left to right.
        """
        if rootNode is None:
            return
        customQueue = queue.Queue()  # Use a queue to keep track of nodes
        customQueue.enqueue(rootNode)  # Start with the root node
        while not customQueue.isEmpty():
            node = customQueue.dequeue()  # Dequeue the current node
            print(node.data, end=', ')  # Print the current node
            if node.leftChild is not None:
                # Enqueue the left child if it exists
                customQueue.enqueue(node.leftChild)
            if node.rightChild is not None:
                # Enqueue the right child if it exists
                customQueue.enqueue(node.rightChild)
        return "Level Order Traversal is Good"

    def search(self, rootNode, nodeValue):
        """
        Search for a node with the given value in the BST.
        """
        if rootNode is None:
            return 'Binary Search Tree is Empty.'
        if rootNode.data == nodeValue:
            return 'Found'  # Node found
        elif nodeValue < rootNode.data:
            if rootNode.leftChild is None:
                return 'Not Found'  # Node not found in the left subtree
            else:
                # Recursively search in the left subtree
                return self.search(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                return 'Not Found'  # Node not found in the right subtree
            else:
                # Recursively search in the right subtree
                return self.search(rootNode.rightChild, nodeValue)

    def deleteNode(self, rootNode, nodeValue):
        """
        Delete a node with the given value from the BST.
        """
        if rootNode is None:
            return 'There is nothing to delete'  # Tree is empty

        # Step 1: Find the node to delete
        if nodeValue < rootNode.data:
            # Recursively search in the left subtree
            rootNode.leftChild = self.deleteNode(rootNode.leftChild, nodeValue)
        elif nodeValue > rootNode.data:
            # Recursively search in the right subtree
            rootNode.rightChild = self.deleteNode(rootNode.rightChild, nodeValue)
        else:
            # Step 2: Node to delete is found
            # Case 1: Node is a Leaf Node (No Children)
            if rootNode.leftChild is None and rootNode.rightChild is None:
                rootNode = None  # Simply remove the node

            # Case 2: Node has One Child
            elif rootNode.leftChild is None:
                rootNode = rootNode.rightChild  # Replace with the right child
            elif rootNode.rightChild is None:
                rootNode = rootNode.leftChild  # Replace with the left child

            # Case 3: Node has Two Children
            else:
                # Find the in-order successor (smallest node in the right subtree)
                successor = self.minValueNode(rootNode.rightChild)
                # Copy the successor's value to the current node
                rootNode.data = successor.data
                # Delete the successor node
                rootNode.rightChild = self.deleteNode(rootNode.rightChild, successor.data)

        return rootNode  # Return the updated tree

    def minValueNode(self, Node):
        """
        Find the node with the minimum value in a subtree.
        """
        current = Node
        while current.leftChild is not None:
            current = current.leftChild  # Traverse to the leftmost node
        return current

# Example Usage
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert nodes into the BST
    print(bst.insertNode(4))  # The node has been successfully inserted.
    print(bst.insertNode(3))  # The node has been successfully inserted.
    print(bst.insertNode(5))  # The node has been successfully inserted.
    print(bst.insertNode(1))  # The node has been successfully inserted.
    print(bst.insertNode(2))  # The node has been successfully inserted.
    print(bst.insertNode(6))  # The node has been successfully inserted.

    # Binary Search Tree
    #       4
    #      / \
    #     3   5
    #    / \   \
    #   1   2   6

    # Perform traversals
    print("Pre-order Traversal:")
    bst.preOrderTraversal(bst.root)  # Output: 4, 3, 1, 2, 5, 6,

    print("\nIn-order Traversal:")
    bst.inOrderTraversal(bst.root)  # Output: 1, 2, 3, 4, 5, 6,

    print("\nPost-order Traversal:")
    bst.postOrderTraversal(bst.root)  # Output: 2, 1, 3, 6, 5, 4,

    print("\nLevel-order Traversal:")
    print(bst.levelOrderTraversal(bst.root))  # Output: 4, 3, 5, 1, 2, 6, Level Order Traversal is Good

    # Search for nodes
    print(bst.search(bst.root, 1))  # Output: Found
    print(bst.search(bst.root, 6))  # Output: Found
    print(bst.search(bst.root, 60))  # Output: Not Found

    