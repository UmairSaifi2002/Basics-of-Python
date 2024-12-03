# import array

# my_array = array.array('i',[1,2,3,4,5])
# print(my_array) # array('i', [1, 2, 3, 4, 5])

# import numpy as np
# np_array = np.array([],dtype=int) 
# print(np_array)
# np_array1 = np.array([1,2,3,4,5,6]) 
# print(np_array1)

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # insertion at different position in array
# a1 = array.array('i',[11,22,33,44,55])
# print(a1)
# a1.insert(0,9)
# print(a1)
# a1.insert(3,6)
# print(a1)
# a1.insert(7,7)
# print(a1)

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # Traversal on array
# t1 = array.array('i',[1,2,3,4,5,6])
# for i in t1:
#     print(i,end=', ')
# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # Accessing element in an array
# from array import *
# def accessElement(array,index):
#     if index >= len(array):
#         print("There is not any element present at this index.")
#     else:
#         print(array[index])
# e1 = array('i',[1,2,3,4,5,76,8])
# print()
# accessElement(e1,4)
# accessElement(e1,3)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Searching in an araay
# Linear Search
# from array import *
# my_array = array('u',['u','m','a','i','r'])
# search = 'B'
# exist = False
# for i in my_array:
#     if search == i:
#         exit = True
#         break
# if exist:
#     print('Present')
# else:
#     print('Not Present')

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# remove element from the array

# from array import *

# arr = array('i',[1,2,3,3,4,5])
# print(arr)
# # syntax -> array_name.remove(element)
# arr.remove(3)
# print(arr)
# arr.remove(1)
# print(arr)


