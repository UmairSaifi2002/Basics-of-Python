# Quick Quiz: Write a program to print 1 to 50 using a while loop.
# i = 1
# while i <= 50:
#     print(i)
#     i = i+1

# -------------------------------------------------------------------------------------------------------------------------------

# Quick Quiz: Write a program to print the content of a list using while loops.
# list = [1,2,3,4]
# i = 0
# while i < len(list):
#     print(list[i])
#     i=i+1

# -------------------------------------------------------------------------------------------------------------------------------

# Ques 1. Write a program to print multiplication table of a given number using for loop.
# num = int(input())
# Using While Loop
# i = 1
# while i <= 10:
#     print(f"{num} X {i} = {num*i}")
#     i = i+1
# Using For Loop
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# -------------------------------------------------------------------------------------------------------------------------------

# Ques 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# Using while loop
# i = 0
# while i < len(l):
#     name = l[i]
#     if(name[0] == 'S'):
#         print(f"Hello {name}")
#     i=i+1

# using for loop
# for i in range(0,len(l)):
#     name = l[i]
#     if(name[0] == 'S'):
#         print(f"Hello {name}")

# -------------------------------------------------------------------------------------------------------------------------------

# Ques 3. Write a program to find whether a given number is prime or not.
# num = int(input("Enter a number: "))

# # Handle edge cases for 0, 1, and 2
# if num <= 1:
#     print(f"{num} is NOT a Prime Number.")
# elif num == 2:
#     print(f"{num} is a Prime Number.")
# else:
#     # Assume the number is prime
#     prime = True

#     # Check divisors from 2 to sqrt(num)
#     for i in range(2, int(num ** 0.5) + 1):  # Efficient range
#         if num % i == 0:
#             prime = False
#             break

#     # Output result
#     if prime:
#         print(f"{num} is a Prime Number.")
#     else:
#         print(f"{num} is NOT a Prime Number.")

# -------------------------------------------------------------------------------------------------------------------------------

# Ques 4. Write a program to find the sum of first n natural numbers using while loop.
# num = int(input())
# i = 1
# sum = 0
# while i <= num:
#     sum = sum+i
#     i = i+1

# print(sum)

# -------------------------------------------------------------------------------------------------------------------------------

# Ques 5. Write a program to calculate the factorial of a given number using for loop.

# num = int(input())

# fact = 1
# if(num == 1):
#     fact = 1
# elif(num == 2):
#     fact = 2
# else:
#     for i in range(2, num+1):
#         fact = fact * i
# print(fact)

# -------------------------------------------------------------------------------------------------------------------------------

# Ques 6 :- Print a pattern
#  *
# ***
#***** for n = 3

# Brute Force Approach - O(n^2)
# n = 3
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()

# Now think about it again - O(n)
# n = 3
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1))

# -------------------------------------------------------------------------------------------------------------------------------

# Ques 7. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# n = 3
# for i in range(1,n+1):
#     print("*"*(i))

# -------------------------------------------------------------------------------------------------------------------------------

# Ques 8. Write a program to print the following star pattern.
# ***
# * * for n = 3
# ***

# Brute force Approach - O(n^2)
# n = 3
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i == 1 or i == n or j == 1 or j == n):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# now think about it again - O(n)
# n = 3
# for i in range(1,n+1):
#     if(i == 1 or i == n):
#         print("*"*n,end="")
#     else:
#         print("*"+" "*(n-2)+"*",end="")
#     print()
