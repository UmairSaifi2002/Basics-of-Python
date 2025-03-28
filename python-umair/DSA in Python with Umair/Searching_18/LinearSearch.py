# Linear Search

def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [3,4,5,2,7,8,4,1,0,6,9]
target = 5

if LinearSearch(arr, target) != -1:
    print(f"Target found at index {LinearSearch(arr, target)}")
else:
    print("Target not found")

# Time Complexity: O(n)
