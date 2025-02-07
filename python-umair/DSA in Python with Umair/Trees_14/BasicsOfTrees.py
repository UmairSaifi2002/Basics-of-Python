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