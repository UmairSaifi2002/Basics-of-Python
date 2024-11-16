# Here we Define the Function Definition
# def func():
#     print("Hello")
# func() # here we call the function so, it will execute its definition

# ---------------------------------------------------------------------------------------------------------------------------

# Quick Quiz: Write a program to greet a user with “Good day” using functions.

# def greet():
#     print("Good Day User")
# greet()

# now make it by using the input form the user
# name = input("Enter your name: ")
# def greet(name): # 'name' here is a parameter
#     print(f"Good Day, {name}!")
# greet(name) # here we pass an argument

# now see how to create/set a Default Parameter Value
# def greet(name = "Umair Saifi"):
#     print(f"Good Day, {name}!")
# greet() # not passing the argument
# greet("Mohammad")

# ---------------------------------------------------------------------------------------------------------------------------
# Learn about Recursion using the function
# def recurrsion(n):
#     if n==1 or n ==0:
#         return 1
#     else:
#         return n*recurrsion(n-1)
# print(recurrsion(1))
# print(recurrsion(2))
# print(recurrsion(3))
# print(recurrsion(4))

# ---------------------------------------------------------------------------------------------------------------------------
# Do some Questions on function/Recurrsion

# Ques 1. Write a program using functions to find greatest of three numbers.
# first = int(input())
# second = int(input())
# third = int(input())

# def greatest(first,second,third):
#     if first > second:
#         if first > third:
#             return first
#         else:
#             return third
#     else:
#         if second > third :
#             return second
#         else:
#             return third

# print(greatest(first,second,third))

# ---------------------------------------------------------------------------------------------------------------------------
# Ques 2. Write a python program using function to convert Celsius to Fahrenheit.
# temp = int(input())

# def celToFah(temp):
#     temp = (temp*(9/5)) + 32
#     return temp

# print(celToFah(temp))

# ---------------------------------------------------------------------------------------------------------------------------
# Ques 3. Write a recursive function to calculate the sum of first n natural numbers.
# num = int(input())

# def sumToN(num):
#     if num == 1:
#         return 1
#     return num + sumToN(num-1)

# print(sumToN(num))

# ---------------------------------------------------------------------------------------------------------------------------
# Ques 4. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

# num = int(input())

# def pattern(n):
#     while n > 0:
#         print("*"*n)
#         n = n-1

# pattern(num)

# ---------------------------------------------------------------------------------------------------------------------------
# Ques 5. Write a python function to remove a given word from a list ad strip it at the same time.
# def rem(l,word):
#     n = []
#     for item in l:
#         if not(item is word):
#             n.append(item.strip(word))
#             return n
# l = ["umair","saifi","air","aerial"]
# print(rem(l,"air"))
