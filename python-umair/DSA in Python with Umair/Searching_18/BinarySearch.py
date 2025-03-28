# We will Learn about Binary Search
# Binary Search ONLY works on SORTED ARRAYS

def BinarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    middle = left + int((right-left)/2)
    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        left = middle + 1
        BinarySearch(arr[left:right+1],target)
    else:
        right = middle - 1
        BinarySearch(arr[left:right+1],target)
    return -1


arr = [1,2,3,4,5,6,7,8,9,10]
target = 5

print(BinarySearch(arr, target))

# Time Complexity: O(log2n)

