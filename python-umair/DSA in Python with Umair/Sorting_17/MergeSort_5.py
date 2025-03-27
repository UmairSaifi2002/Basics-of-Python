# Merge Sort Algorithm

def merge(arr, l, m, r):
    # Calculate the size of the two temporary arrays
    n1 = m - l + 1
    n2 = r - m

    # Create two temporary arrays using list comprehension
    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + 1 + j] for j in range(n2)]

    # Initialize indexes for sorting
    i = 0  # Index for the first temporary array
    j = 0  # Index for the second temporary array
    k = l  # Initial index from where the sorted elements will be stored

    # Merge the temporary arrays back into the original array
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1

    # Copy any remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1

def mergeSort(arr, l, r):
    # Base case: if the array has only one element or is empty
    if l < r:
        # Find the middle point to divide the array into two halves
        m = (l + (r - 1)) // 2

        # Recursively sort the first half
        mergeSort(arr, l, m)

        # Recursively sort the second half
        mergeSort(arr, m + 1, r)

        # Merge the sorted halves
        merge(arr, l, m, r)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")

mergeSort(arr, 0, n - 1)

print("\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
