# Insertion Sort is a simple sorting algorithm that works by repeatedly inserting the unsorted elements into the correct position in the sorted portion of the array.

# Lets deep dive into the algorithm

# Insertion Sort Algorithm

# 1. Compare the current element with the previous element
# 2. If the current element is smaller than the previous element, swap them
# 3. Repeat until the array is sorted

def InsertionSort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Start from the second element (index 1) since the first element is trivially sorted
    for i in range(1, n):
        # Store the current element to be compared and potentially inserted into the sorted portion
        key = arr[i]
        
        # Initialize j to the index before the current element
        j = i - 1
        
        # Move elements greater than key to one position ahead
        # This creates space for the key to be inserted in its correct position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key into its correct position in the sorted portion
        arr[j + 1] = key
    
    # Return the sorted array (though the original array is modified in-place)
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
InsertionSort(arr)
print("Sorted array:", arr)

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# that's who the algo sort the arr
# small example
# 64, 34, 25, 12
# j    i

# 34, 64, 25, 12
# j	 i

# 25, 64, 34, 12
#      j   i

# 25, 34, 64, 12
# j  	     i

# 12, 34, 64, 25
#      j       i

# 12, 25, 64, 34
# 	 j   i

# 12, 25, 34, 64 