# Minimal Tree
# Given a sorted Array with unique integer element, write an algorithm to create a binary search treewith minimal height

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    mid = int(len(sortedArray)/2)
    left = minimalTree(sortedArray[:mid])
    right = minimalTree(sortedArray[mid+1:])
    return BSTNode(sortedArray[mid], left, right)

sortedArray = [1,2,3,4,5,6,7,8,9,10,11,12]
minimalTree(sortedArray)
