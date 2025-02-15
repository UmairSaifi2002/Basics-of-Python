# Now we will Learn about the AVL Tree
# An AVL Tree (Adelson-Velsky and Landis Tree) is a self-balancing Binary Search Tree (BST) where the difference between the heights of the left 
# and right subtrees (called the balance factor) of any node is at most 1. 
# This balancing ensures that the tree remains approximately balanced, guaranteeing O(log n) time complexity for search, insert, and delete operations.

# Key Properties:
# Binary Search Tree Property: Left subtree < Root < Right subtree.
# Balance Factor: For any node, balance factor = height(left subtree) - height(right subtree). It must be -1, 0, or 1.
# Balancing: If the balance factor violates the AVL property, the tree performs rotations to restore balance.

# Balanced Height: Ensures O(log n) time complexity for operations.
# Efficient Operations: Ideal for scenarios requiring frequent insertions and deletions while maintaining search efficiency.

# Real-World Applications:
# Databases (indexing).
# Memory allocation in operating systems.
# Implementing ordered maps and sets.

# When the balance factor of a node violates the AVL property, rotations are performed to restore balance. There are four types of rotations:
# Left Rotation (LL Rotation):
#       Used when the right subtree is heavier.
#       Example: Inserting a node into the right subtree of the right child.
# Right Rotation (RR Rotation):
#       Used when the left subtree is heavier.
#       Example: Inserting a node into the left subtree of the left child.
# Left-Right Rotation (LR Rotation):
#       Used when the left subtree is heavier, and the insertion happens in the right subtree of the left child.
#       Combines a left rotation followed by a right rotation.
# Right-Left Rotation (RL Rotation):
#       Used when the right subtree is heavier, and the insertion happens in the left subtree of the right child.
#       Combines a right rotation followed by a left rotation.

import sys

# Add the folder containing BasicOfQueue.py to sys.path
queue_folder_path = r"c:\\Users\\umair\\OneDrive\\Desktop\\Programming\\Basics-of-Python\\python-umair\\DSA in Python with Umair\\Queue_11"
sys.path.append(queue_folder_path)

# Import the file
import BasicOfQueue as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    # now create all four function of traversal 
    def preOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.leftChild)
        self.preOrderTraversal(rootNode.rightChild)
    
    def inOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        self.inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        self.inOrderTraversal(rootNode.rightChild)

    def postOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        self.postOrderTraversal(rootNode.leftChild)
        self.postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)
    
    def levelOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            node = customQueue.dequeue()
            print(node.data)
            if node.leftChild is not None:
                customQueue.enqueue(node.leftChild)
            if node.rightChild is not None:
                customQueue.enqueue(node.rightChild)
    
    # also create Search method to find the node
    def searchNode(self, rootNode,  nodeValue):
        if rootNode is None:
            return
        if rootNode.data == nodeValue:
            return 'Successfully Found'
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            node = customQueue.dequeue()
            if node.leftChild is not None:
                if node.leftChild.data == nodeValue:
                    return 'Successfully Found'
                else:
                    customQueue.enqueue(node.leftChild)
            if node.rightChild is not None:
                if node.rightChild.data == nodeValue:
                    return 'Successfully Found'
                else:
                    customQueue.enqueue(node.rightChild)
    
    # insertion in AVL Tree
    # it only have two cases
    # Case 1: When Rotation is not Required - It is a case just like the insertion in Binary Search Tree
    # Case 2: When Rotation is Required - but when the Rotation is required then it have four ways
    #         1, LL - left left condition - In this condition we have to Identify the Disbalanced Node and perform Right Rotation
    #         2, LR - left right condition - In this condition we have to Identify the Disbalanced Node and perform first left rotation to leftChild of Disbalanced Node and then right Rotation to the  Disbalanced Node
    #         3, RL - right left condition - In this Condition 
    #         4, RR - right right condition

    # We have to create helper function's 
    def getHeight(self, rootNode):
        if rootNode is None:
            return 0
        return rootNode.height
    
    def getBalanceFactor(self, node):
        if node is None:
            return 0
        return self.getBalanceFactor(node.leftChild) - self.getBalanceFactor(node.rightChild)
    
    def rightRotate(self, disBalancedNode):
        # Step 1: Identify the new root (left child of disbalanced node)
        newRoot = disBalancedNode.leftChild
        # Step 2: Reassign the right child of newRoot to the left child of disBalancedNode
        disBalancedNode.leftChild = newRoot.rightChild
        # Step 3: Make disBalancedNode the right child of newRoot
        newRoot.rightChild = disBalancedNode
        # Step 4: Update heights of the rotated nodes
        disBalancedNode.height = 1 + max(self.getHeight(disBalancedNode.leftChild), self.getHeight(disBalancedNode.rightChild))
        newRoot.height = 1 + max(self.getHeight(newRoot.leftChild), self.getHeight(newRoot.rightChild))
        # Step 5: Return the new root (to be connected to the parent)
        return newRoot

    def leftRotate(self, disBalancedNode):
        # Step 1: Identify the root (right child of disBalanced node)
        newRoot = disBalancedNode.rightChild
        # Step 2: Reassign the right Child of newRoot to the right Child of disBalancedNode
        disBalancedNode.rightChild = newRoot.leftChild
        # Step 3: Make disBalancedNode the left Child of newRoot
        newRoot.leftChild = disBalancedNode
        # Step 4: Update heights of the rotated nodes
        disBalancedNode.height = 1 + max(self.getHeight(disBalancedNode.leftChild), self.getHeight(disBalancedNode.rightChild))
        newRoot.height = 1 + max(self.getHeight(newRoot.leftChild), self.getHeight(newRoot.rightChild))
        # Step 5: Return the new root (to be connected to the parent)
        return newRoot
    
    # The insert Method
    def insert(self, root, key):
        # Step 1: Perform standard BST insertion
        if root is None:
            return TreeNode(key)
        elif key < root.data:
            root.leftChild = self.insert(root.leftChild, key)
        else:
            root.rightChild = self.insert(root.rightChild, key)
        # Step 2: Update the height of the current node
        root.height = 1 + max(self.getHeight(root.leftChild), self.getHeight(root.rightChild))
        # Step 3: Get the balance factor of the current node
        balance = self.getBalanceFactor(root)
        # Step 4: Perform rotations if the node is unbalanced
        # Case 1: Left-Left (LL) Imbalance
        if balance > 1 and key < root.leftChild.data:
            return self.rightRotate(root)
        # Case 2: Right-Right (RR) Imbalance
        if balance < -1 and key > root.rightChild.data:
            return self.leftRotate(root)
        # Case 3: Left-Right (LR) Imbalance
        if balance > 1 and key > root.leftChild.data:
            root.leftChild = self.leftRotate(root.leftChild)
            return self.rightRotate(root)
        # Case 4: Right-Left (RL) Imbalance
        if balance < -1 and key < root.rightChild.data:
            root.rightChild = self.rightRotate(root.rightChild)
            return self.leftRotate(root)
        # Step 5: Return the updated root
        return root 

if __name__ == "__main__":
    avl = AVLTree()
    
