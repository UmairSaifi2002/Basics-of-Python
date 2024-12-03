# What will be the output of the following code block?

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")

'''
Overall explanation
The given code block first modifies the arr list using a for loop and then prints the elements of the modified list. Here's the step-by-step execution of the code:

Iterate through the list using a for loop with a range from 1 to 5 (6 not included). For each i, the value of arr[i] is assigned to arr[i - 1]. This operation effectively shifts each element to the left by one position except for the first element.

After the loop, arr becomes: [2, 3, 4, 5, 6, 6]

Iterate through the modified list using another for loop with a range from 0 to 5 (6 not included). The print() function is called with the end = " " parameter, which prints each element followed by a space instead of a newline.

So, the output of the code block will be:

2 3 4 5 6 6 
Note the trailing space after the last element.
'''