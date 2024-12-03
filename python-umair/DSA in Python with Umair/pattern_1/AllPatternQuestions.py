'''
Basic triangle Pattern
ex - 1
* 
* * 
* * * 
* * * *
'''
# row = int(input('row : '))
# i = 1
# j = 1
# for i in range(row):
#     for j in range(i+1):
#         print('* ',end='')
#     print('')

''' 
ex - 2
1
12
123
1234
'''
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end='')
#     print()

'''
ex - 3
1
22
333
4444
'''
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end='')
#     print()

'''
ex - 4
****
***
**
*
'''
# n = int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*',end='')
#     print()

'''
ex - 5
*
***
*****
*******
'''
# for i in range(4):
#     for j in range(2*i+1):
#         print('*',end='')
#     print()

'''
ex - 6
*******
*****
***
*
'''
# n = 4
# for i in range(n-1,0-1,-1):
#     for j in range(2*i+1):
#         print('*',end='')
#     print()

'''
ex - 7
   *
  ***
 *****
*******
'''
# n = 4
# for i in range(n):
#     for j in range(n,i+1,-1):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()

'''
ex - 8
*******
 *****
  ***
   *
'''
# n = 4
# for i in range(n-1,0-1,-1):
#     for j in range(i+1,n):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()

'''
ex - 9
   *
  ***
 *****
*******
*******
 *****
  ***
   *
'''
# n = 4
# for i in range(n):
#     for j in range(n-1,i,-1):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()
# for i in range(n-1,0-1,-1):
#     for j in range(i,n-1):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()

'''
ex - 10
   *
  ***
 *****
*******
 *****
  ***
   *
'''
# n = 3
# for i in range(n):
#     for j in range(n-1,i,-1):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()
# for i in range(n-2,0-1,-1):
#     for j in range(i,n-1):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('*',end='')
#     print()

'''
ex - 11
*
**
***
****
***
**
*
'''
# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print()
# for i in range(n-1):
#     for j in range(n-1,i,-1):
#         print('*',end='')
#     print()

'''
ex - 12
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''
# n = 10
# for i in range(n):
#     for j in range(i+1):
#         if (((i+j) % 2) == 0):
#             print('1',end='')
#         else:
#             print('0',end='')
#     print()

'''
ex - 13
1      1
12    21
123  321
12344321
'''
# n = 6
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end='')
#     for j in range(2*(n-(i+1))):
#         print(' ',end='')
#     for j in range(i+1):
#         print(i+1-j,end='')
#     print()

'''
ex - 14
1
2 3
4 5 6
7 8 9 10
'''
# n = 4
# a = 1
# for i in range(n):
#     for j in range(i+1):
#         print(a,end='')
#         a = a+1
#     print()

'''
ex - 15
A
AB
ABC
ABCD
'''
# n= 4
# char = 'A'
# for i in range(n):
#     for j in range(i+1):
#         print(char,end='')
#         char = chr(ord(char) + 1) # most important
#     char = 'A'
#     print()

'''
ex - 16
ABCD
ABC
AB
A
'''
# n=4
# char = 'A'
# for i in range(n,0,-1):
#     for j in range(i):
#         print(char,end='')
#         char = chr(ord(char)+1)
#     print()
#     char = 'A'

'''
ex - 17
A
BB
CCC
DDDD
'''
# n = 4
# char  = 'A'
# for i in range(n):
#     for j in range(i+1):
#         print(char,end='')
#     char = chr(ord(char)+1)
#     print()

'''
ex - 18
...A
..ABA
.ABCBA
ABCDCBA
'''
# n = 4
# char = 'A'
# for i in range(n):
#     for j in range(n-1,i,-1):
#         print(' ',end='')
#     for j in range(i+1):
#         print(char,end='')
#         char = chr(ord(char)+1)
#     char = chr(ord(char)-2)
#     for j in range(i):
#         print(char,end='')
#         char = chr(ord(char)-1)
#     char = 'A'
#     print()

'''
ex - 19
   1
  121
 12321
1234321
'''
# n = 4
# for i in range(n):
#     for j in range(n-1,i,-1):
#         print(' ',end='')
#     for j in range(i+1):
#         print(j+1,end='')
#     for j in range(i):
#         print(i-j,end='')
#     print()

'''
ex - 20
E
DE
CDE
BCDE
ABCDE
'''
# n = 5
# char = chr(65+n-1)
# # print(char)
# for i in range(n):
#     for j in range(i+1):
#         print(char,end='')
#         char = chr(ord(char)+1)
#     char = chr(65+n-i-2)
#     print()

'''
ex - 21
********
***  ***
**    **
*      *
**    **
***  ***
********
'''
# n = 5
# for i in range(n):
#     for j in range(n,i,-1): # star
#         print('*',end='')
#     for j in range(2*i): # space
#         print(' ',end='')
#     for j in range(n,i,-1): # star
#         print('*',end='')
#     print()
# for i in range(n-1):
#     for j in range(i+2): # star
#         print('*',end='')
#     for j in range(2*(n-1-i-1)): # space
#         print(' ',end='')
#     for j in range(i+2): # star
#         print('*',end='')
#     print()

# for i in range(n):
#     for j in range(n,i,-1): # star
#         print('*',end='')
#     for j in range(2*i): # space
#         print(' ',end='')
#     for j in range(n,i,-1): # star
#         print('*',end='')
#     print()
# for i in range(n-1):
#     for j in range(i+2): # star
#         print('*',end='')
#     for j in range(2*(n-1-i-1)): # space
#         print(' ',end='')
#     for j in range(i+2): # star
#         print('*',end='')
#     print()

'''
ex - 22
*      *
**    **
***  ***
********
***  ***
**    **
*      *
'''
# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     for j in range(2*(n-i-1)):
#         print(' ',end='')
#     for j in range(i+1):
#         print('*',end='')
#     print()
# for i in range(n-1):
#     for j in range(i,n-1):
#         print('*',end='')
#     for j in range(2*(i+1)):
#         print(' ',end='')
#     for j in range(i,n-1):
#         print('*',end='')
#     print()

'''
ex - 23
****
*  *
*  *
****
'''
# n = 4
# for i in range(n):
#    for j in range(n):
#       if i==0 or i==n-1 or j==0 or j==n-1:
#          print('*',end='')
#       else:
#          print(' ',end='')
#    print()
      
'''
4444444
4333334
4322234
4321234
4322234
4333334
4444444
'''
# n = 4  # Grid si(2 * n - 2) - jze parameter

# # Loop through rows
# for i in range(2 * n - 1):
#     # Loop through columns
#     for j in range(2 * n - 1):
#         # Calculate value based on minimum distance from edges
#         top = i
#         bottom = j
#         left = (2*n-2)-i
#         right = (2*n-2)-j
#         value = n - min(top, bottom, left, right)
#         print(value, end=" ")  # Print value with a space
#     print()  # Move to the next row

