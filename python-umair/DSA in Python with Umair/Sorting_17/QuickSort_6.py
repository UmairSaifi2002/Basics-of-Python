# Quik Sort
def pivot_element(arr):
    # Choose the first element as the pivot
    pivot = arr[0]
    
    # Initialize the index for the next swap position
    swap_index = 0
    
    # Iterate through the array starting from the second element
    i = 1
    while i < len(arr):
        # If the current element is less than the pivot
        if arr[i] < pivot:
            # Increment the swap index
            swap_index += 1
            # Swap the current element with the element at the swap index
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
        # Move to the next element
        i += 1
    
    # Swap the pivot element with the element at the swap index
    arr[0], arr[swap_index] = arr[swap_index], arr[0]
    
    # Return the index of the pivot element
    return swap_index

def quick_sort(arr):
    # Base case: if the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Partition the array and get the pivot index
    pivot_index = pivot_element(arr)
    
    # Recursively sort the left part of the array (elements less than the pivot)
    left = quick_sort(arr[:pivot_index])
    
    # Recursively sort the right part of the array (elements greater than the pivot)
    right = quick_sort(arr[pivot_index+1:])
    
    # Combine the sorted left part, the pivot, and the sorted right part
    return left + [arr[pivot_index]] + right

# Example usage
print(quick_sort([5, 4, 3, 2, 1]))
