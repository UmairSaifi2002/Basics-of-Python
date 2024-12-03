# What will be the output of the following code block?

a=[1,2,3,4,5]
print(a[3:0:-1])

'''
The given code block performs a slice operation on the list a using the syntax a[start:stop:step]. 
In this case, start is 3, stop is 0, and step is -1. 
This slice operation creates a new list containing elements from the original list, 
starting at index 3, going until index 0 (not inclusive), and selecting every element with a step of -1 (moving in reverse).

So, the output of the code block will be:

csharpCopy code
[4, 3, 2]
The slice operation picks the elements at indices 3, 2, and 1 from the original list.
'''