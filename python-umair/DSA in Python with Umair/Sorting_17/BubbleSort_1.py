# Bubble Sort is also called as Sinking Sort
# It is a simple sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
# This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# Lets deep dive into the algorithm

# Bubble Sort Algorithm

# 1. Compare adjacent elements

def bubble_sort(arr):
    # Get the length of the array (subtracting 1 to prevent index out-of-bounds errors)
    n = len(arr) - 1
    
    # Outer loop: Iterate through each element of the array
    # The loop runs 'n' times (once for each element)
    for i in range(n):
        # Inner loop: Compare adjacent elements up to the unsorted portion
        # After each complete pass, the largest element "bubbles up" to its correct position
        # So we reduce the range by 'i' each time (since last 'i' elements are already sorted)
        for j in range(n - i):
            # Compare current element with the next element
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Return the sorted array (though the original array is modified in-place)
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
