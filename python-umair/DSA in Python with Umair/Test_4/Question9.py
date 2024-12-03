arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())

'''
Here's the step-by-step execution of the code:

i = 0: The last element of the first row (arr[0]) is 4. The pop() method removes and returns 4, and the first row becomes [1, 2, 3]. The print() function outputs 4.

i = 1: The last element of the second row (arr[1]) is 7. The pop() method removes and returns 7, and the second row becomes [4, 5, 6]. The print() function outputs 7.

i = 2: The last element of the third row (arr[2]) is 11. The pop() method removes and returns 11, and the third row becomes [8, 9, 10]. The print() function outputs 11.

i = 3: The last element of the fourth row (arr[3]) is 15. The pop() method removes and returns 15, and the fourth row becomes [12, 13, 14]. The print() function outputs 15.

So, the output of the code block will be: 4 7 11 15
'''