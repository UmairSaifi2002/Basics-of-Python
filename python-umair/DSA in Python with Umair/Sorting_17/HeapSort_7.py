# Heap Sort

def heapify(arr, n, i):
    # First, assume the root element (at index i) is the largest
    largest = i
    # Calculate the index of the left child
    left = 2 * i + 1
    # Calculate the index of the right child
    right = 2 * i + 2
    # Check if left child exists and is greater than the current largest
    if left < n and arr[left] > arr[largest]:
        # Update largest if left child is greater
        largest = left
    # Check if right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        # Update largest if right child is greater
        largest = right
    # If largest is not the root, swap them
    if largest != i:
        # Swap the elements
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build a maxheap
    # Start from the last parent node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # One by one extract elements from the heap
    for i in range(n-1, 0, -1):
        # Swap the root (largest element) with the last element
        arr[i], arr[0] = arr[0], arr[i]
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Given array is:", arr)

heap_sort(arr)
print("Sorted array is:", arr)

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

