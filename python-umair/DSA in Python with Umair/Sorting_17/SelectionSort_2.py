# Selection Sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

# Lets deep dive into the algorithm

# Selection Sort Algorithm

# 1. Find the smallest element in the unsorted portion of the list
# 2. Swap it with the first element
# 3. Repeat until the list is sorted

def SelectionSort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Iterate through each element of the array
    # The outer loop represents the sorted portion of the array growing from left to right
    for i in range(n):
        # Assume the current position is the minimum
        min_index = i
        
        # Inner loop: Find the actual minimum element in the unsorted portion
        # Start from i+1 since we're comparing with the current element at i
        for j in range(i + 1, n):
            # If a smaller element is found, update min_index
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted portion
        # This places the minimum element in its correct position in the sorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # Return the sorted array (though the original array is modified in-place)
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
SelectionSort(arr)
print("Sorted array:", arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)