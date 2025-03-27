# Bucket Sort is a sorting algorithm that works by distributing the elements of an array into a number of buckets.

# Lets deep dive into the algorithm

# Bucket Sort Algorithm
import math
# from InsertionSort_3 import InsertionSort

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

def BucketSort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Calculate the number of buckets to use
    # A common heuristic is to use the square root of the number of elements
    no_of_buckets = round(math.sqrt(n))
    
    # Find the maximum value in the array to determine the range of values
    max_value = max(arr)
    
    # Initialize an empty list for each bucket
    bucket_array = []
    for i in range(no_of_buckets):
        bucket_array.append([])
    
    # Distribute the elements of the array into the buckets
    for j in arr:
        # Calculate the index of the bucket where the current element should go
        # This is done by scaling the element value to the number of buckets
        bucket_index = math.ceil(j * no_of_buckets / max_value)
        bucket_array[bucket_index - 1].append(j)
    
    # Sort each bucket using Insertion Sort
    for i in range(no_of_buckets):
        bucket_array[i] = InsertionSort(bucket_array[i])
    
    # Concatenate the sorted buckets into a single sorted array
    result_array = []
    for i in range(no_of_buckets):
        # result_array.extend(bucket_array[i])  # This line is commented out but does the same thing as the next line
        result_array += bucket_array[i]  # Concatenate the sorted elements from each bucket
    
    # Return the fully sorted array
    return result_array

'''
with negative values

def BucketSort(arr):
    if not arr:
        return arr
    
    # Step 1: Determine the range of values
    min_value = min(arr)
    max_value = max(arr)
    
    # Step 2: Normalize the values
    offset = -min_value  # Offset to shift all values to non-negative
    range_of_values = max_value - min_value + 1
    
    # Step 3: Determine the number of buckets
    no_of_buckets = round(math.sqrt(len(arr)))
    
    # Step 4: Initialize buckets
    bucket_array = [[] for _ in range(no_of_buckets)]
    
    # Step 5: Distribute elements into buckets
    for j in arr:
        normalized_value = j + offset
        bucket_index = math.floor(normalized_value * no_of_buckets / range_of_values)
        bucket_array[bucket_index].append(j)
    
    # Step 6: Sort each bucket
    for i in range(no_of_buckets):
        bucket_array[i] = InsertionSort(bucket_array[i])
    
    # Step 7: Concatenate buckets
    result_array = []
    for i in range(no_of_buckets):
        result_array.extend(bucket_array[i])
    
    return result_array
'''

arr = [3, 6, 2, 1, 8, 7, 5, 4]
print(BucketSort(arr))

# Time Complexity: O(n^2)
# Space Complexity: O(n)
