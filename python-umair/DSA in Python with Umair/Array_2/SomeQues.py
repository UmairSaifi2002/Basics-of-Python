# 1. Create an array and Traverse

# # Creating an array
# from array import *
# a = array('i',[1,2,3,4])
# # Traversing
# for i in a:
#     print(i)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 2. Access individual elements through indeces

# from array import *
# a = array('i',[1,2,3,4,5,6])
# print(a[0])
# print(a[4])
# print(a[8])

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 3. Append any value to the array using append() method

# from array import *
# a = array('i',[1,2,3,4,5,6])
# print(a)
# a.append(7)
# print(a)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 4. Insert value in an array using insert() method

# from array import *
# a = array('i',[1,2,3,4,5,6])
# print(a)
# a.insert(0,4)
# print(a)
# a.insert(4,65)
# print(a)
# a.insert(9,78)
# print(a)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 5. Extend Python array using extend() method

# from array import *
# a = array('i',[1,2,3,4,5])
# print(a)
# a.extend([6,7,8,9])
# print(a)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 6. Add items from list into array using fromlist() method

# from array import *
# a = array('i',[1,2,3,4,5])
# lists = [10,11,12,13]
# a.fromlist(lists)
# print(a)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 7. Remove any array element using remove() method

# from array import *
# a = array('i',[1,2,3,4,5])
# print(a)
# a.remove(1)
# print(a)
# a.remove(5)
# print(a)
# a.remove(3)
# print(a)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 8. Remove last array element using pop() method

# from array import *
# a = array('i',[1,2,3,4,5])
# print(a)
# a.pop()
# print(a)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 9. Fetch any element through its index using index() method

# from array import *
# a = array('i',[1,2,3,4,5])
# print(a.index(3))

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 10. Reverse a python array using reverse() method

# from array import *
# a = array('i',[1,2,3,4,5])
# a.reverse()
# print(a)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 11. Get array buffer information through bufer_info() method

# from array import *
# a = array('i',[1,2,3,4,5])
# print(a.buffer_info())

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 12. Check for number of occurences of an element using count() method

# from array import *
# a = array('i',[1,2,3,4,5,3,5,4,2,5,6,5])
# print(a.count(1))
# print(a.count(2))
# print(a.count(5))

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 13. Convert array to string using toString() method

# Cancelled

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 14. Convert array to the python list with same element using tolist() method

# import numpy as np
# from array import *

# # Create a NumPy array
# arr = np.array([[1, 2], [3, 4]])
# a = array('i',[1,2,3,4,5])

# # Convert to a Python list using tolist()
# list_arr = arr.tolist()
# ar = a.tolist()

# print(list_arr)  # Output: [[1, 2], [3, 4]]
# print(ar)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 15. Append a string to char array using fromstring() method

# Cancelled

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# 16. Slice elements from an array


