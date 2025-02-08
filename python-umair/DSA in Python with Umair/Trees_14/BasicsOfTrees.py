# A Tree is a non-linear Data Structure with hierarchical relations between its elements without having any Cycle.

# Tree Properties
# 1, Represent hierachical data
# 2, Each nodes having two components : data and link to its sub category
# 3, Base Cateories and sub categories under it

# Tree Termonology
# Root # Edge # Leaf 

# Let Discuss about Binary Tree
# Binary Tree can be implemented using a LinkedList, List

# Take a look to create a tree using LinkedList

# importing Queue
# BasicsOfTrees.py
import sys

# Add the folder containing BasicOfQueue.py to sys.path
queue_folder_path = r"c:\\Users\\umair\\OneDrive\\Desktop\\Programming\\Basics-of-Python\\python-umair\\DSA in Python with Umair\\Queue_11"
sys.path.append(queue_folder_path)

# Import the file
import BasicOfQueue as queue

# Use the function from BasicOfQueue.py
result = queue.Queue()
print(result)  # Output: This is a queue example!
# now we can use queue here as well.

# TreeNode class to represent a node in the Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to perform Inorder Traversal (Left -> Root -> Right)
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Function to perform Preorder Traversal (Root -> Left -> Right)
def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Function to perform Postorder Traversal (Left -> Right -> Root)
def postorder_traversal(root):
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

# Function to calculate the height of the tree
def tree_height(root):
    if root is None:
        return 0
    return max(tree_height(root.left), tree_height(root.right)) + 1

# Function to count the number of nodes in the tree
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Function to perform LevelOrder Traversal
def levelOrder(root):
    if root is None:
        return 
    else:
        customQueue = queue.Queue()  # Use your custom Queue
        customQueue.enqueue(root)    # Enqueue the root node
        while not(customQueue.isEmpty()):
            current_node = customQueue.dequeue()
            print(current_node.val, end=" ")  # Print the value of the current node
            if current_node.left is not None:
                customQueue.enqueue(current_node.left)  # Enqueue left child
            if current_node.right is not None:
                customQueue.enqueue(current_node.right)  # Enqueue right child
    print()
    
# Function to perform searching in a Binary Tree
# We know that Queue always perform better than Stack's 
# so we will use Tree Traversal which using Queue
# so LevelOrder Traversal uses Queue. so, it will suitable for searcing a node in Binary Tree
def search(root, data):
    customQueue = queue.Queue()
    customQueue.enqueue(root)
    while not(customQueue.isEmpty()):
        current_node = customQueue.dequeue()
        if current_node.val == data:
            return True
        else:
            if current_node.left is not None:
                customQueue.enqueue(current_node.left)
            if current_node.right is not None:
                customQueue.enqueue(current_node.right)
    return False

# Function to insert a node in Binary Tree
# so we have to find the vacant spot in Binary Tree
# so it will be possible with the levelOrder Traversing
# so LevelOrder Traversing is important
def insert_node(root, data):
    # If the tree is empty, create a new node and make it the root
    if root is None:
        return TreeNode(data)    
    # Use a queue for Level Order Traversal
    customQueue = queue.Queue()
    customQueue.enqueue(root)    
    while not customQueue.isEmpty():
        current_node = customQueue.dequeue()        
        # Check if the left child is empty
        if current_node.left is None:
            current_node.left = TreeNode(data)
            print(f"Inserted {data} as left child of {current_node.val}")
            break
        else:
            customQueue.enqueue(current_node.left)        
        # Check if the right child is empty
        if current_node.right is None:
            current_node.right = TreeNode(data)
            print(f"Inserted {data} as right child of {current_node.val}")
            break
        else:
            customQueue.enqueue(current_node.right)    
    return root

# Function to delete a node from the Binary Tree
# so how to delete a particular node from the Binary Tree
# so it has three cases 
# one :- only one node is present
# two :- deleting a leaf node
# three :- deleting a node which has a child nodes
# in case one, two deletion takes place normally
# but in case third we have to find a last node 
# and then replace the last node from the node you want to delete
# To Do this all we have to make a helper function
# now we will create a helper function named 'getDeepestNode'
def getDeepestNode(root):
    """
    Finds and returns the value of the deepest node in the Binary Tree.
    
    Args:
        root (TreeNode): The root of the Binary Tree.
    
    Returns:
        int: The value of the deepest node.
    """
    if root is None:
        return None  # If the tree is empty, return None
    else:
        customQueue = queue.Queue()  # Initialize a queue for Level Order Traversal
        customQueue.enqueue(root)    # Enqueue the root node
        while not customQueue.isEmpty():
            root = customQueue.dequeue()  # Dequeue the current node
            # Enqueue the left child if it exists
            if root.left is not None:
                customQueue.enqueue(root.left)
            # Enqueue the right child if it exists
            if root.right is not None:
                customQueue.enqueue(root.right)
        # After the loop, `root` will be the deepest node
        return root.val

# now we will create a helper Function named 'deleteDeepestNode'
def deleteDeepestNode(root, deepestNode):
    """
    Deletes the deepest node in the Binary Tree.
    
    Args:
        root (TreeNode): The root of the Binary Tree.
        deepestNode (int): The value of the deepest node to delete.
    """
    if root is None:
        return  # If the tree is empty, return
    else:
        customQueue = queue.Queue()  # Initialize a queue for Level Order Traversal
        customQueue.enqueue(root)    # Enqueue the root node
        while not customQueue.isEmpty():
            root = customQueue.dequeue()  # Dequeue the current node
            # If the current node is the deepest node, set it to None
            if root.val == deepestNode:
                root = None
                return
            # Check the left child
            if root.left is not None:
                if root.left.val == deepestNode:  # If the left child is the deepest node
                    root.left = None  # Delete the left child
                    return
                else:
                    customQueue.enqueue(root.left)  # Enqueue the left child for further traversal
            # Check the right child
            if root.right is not None:
                if root.right.val == deepestNode:  # If the right child is the deepest node
                    root.right = None  # Delete the right child
                    return
                else:
                    customQueue.enqueue(root.right)  # Enqueue the right child for further traversal

def delete_node(root, data):
    """
    Deletes a node with the given value from the Binary Tree.
    
    Args:
        root (TreeNode): The root of the Binary Tree.
        data (int): The value of the node to delete.
    
    Returns:
        str: A message indicating whether the node was successfully deleted or not.
    """
    if root is None:
        return "The tree is empty. Cannot delete node."
    else:
        customQueue = queue.Queue()  # Initialize a queue for Level Order Traversal
        customQueue.enqueue(root)    # Enqueue the root node
        node_to_delete = None        # To store the node to delete
        deepest_node = None          # To store the deepest node        
        parent_of_deepest = None  # To store the parent of the deepest node
        # Traverse the tree to find the node to delete and the deepest node
        while not customQueue.isEmpty():
            current_node = customQueue.dequeue()            
            # Check if the current node is the one to delete
            if current_node.val == data:
                node_to_delete = current_node            
            # Enqueue the left child if it exists
            if current_node.left is not None:
                customQueue.enqueue(current_node.left)    
                parent_of_deepest = current_node
                deepest_node = current_node.left        
            # Enqueue the right child if it exists
            if current_node.right is not None:
                customQueue.enqueue(current_node.right)  
                parent_of_deepest = current_node 
                deepest_node = current_node.right   
        # If the node to delete was found
        if node_to_delete is not None:
            # Replace the value of the node to delete with the value of the deepest node
            node_to_delete.val = deepest_node.val            
            # Delete the deepest node
            if parent_of_deepest.left == deepest_node:
                parent_of_deepest.left = None
            else:
                parent_of_deepest.right = None

            return "The node has been successfully deleted."
        else:
            return "Failed to delete node from the Binary Tree. Node not found."

def delete(root):
    if root is None:
        return
    delete(root.left)
    delete(root.right)
    root.val = None  # Optional, but good practice
    root.left = None
    root.right = None
    # root = None  #  No need to set root to none here, it's done automatically by Python's garbage collection
    return "The Binary Tree has been successfully deleted."

# Example usage
if __name__ == "__main__":
    # Constructing a binary tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Perform traversals
    print("Inorder Traversal:", inorder_traversal(root))    # Output: [4, 2, 5, 1, 3]
    print("Preorder Traversal:", preorder_traversal(root))  # Output: [1, 2, 4, 5, 3]
    print("Postorder Traversal:", postorder_traversal(root))# Output: [4, 5, 2, 3, 1]

    # Calculate height of the tree
    print("Height of the Tree:", tree_height(root))         # Output: 3

    # Count the number of nodes in the tree
    print("Number of Nodes:", count_nodes(root))            # Output: 5

    # Perform Level Order Traversal
    print("Level Order Traversal:", end=" ")
    levelOrder(root)  # Output: 1 2 3 4 5

    # Search for a node in the Binary Tree
    data = 3 
    print(f'{data} is present in BT -> {search(root, data)}')  

    # Insert a new node
    root = insert_node(root, 6)  # Insert 6 as the left child of 3
    root = insert_node(root, 7)  # Insert 7 as the right child of 3

    # Perform Level Order Traversal after insertion
    print("\nLevel Order Traversal after insertion:", end=" ")
    levelOrder(root)  # Output: 1 2 3 4 5 6 7

    # Get the deepest node
    deepestNode = getDeepestNode(root)
    print(f"\nDeepest Node: {deepestNode}")  # Output: Deepest Node: 5

    # Delete the deepest node
    deleteDeepestNode(root, deepestNode)

    # Perform Level Order Traversal after deletion
    print("Level Order Traversal after deletion:", end=" ")
    levelOrder(root)  # Output: 1 2 3 4 5 6

    # Delete a node
    result = delete_node(root, 2)  # Delete node with value 2
    print(result)  # Output: The node has been successfully deleted.

    # Perform Level Order Traversal after deletion
    print("Level Order Traversal after deletion:", end=" ")
    levelOrder(root)  # Output: 1 6 3 4 5

    # Deleting whole Binary Tree
    delete(root)
    levelOrder(root)
