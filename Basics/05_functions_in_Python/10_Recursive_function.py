# Recursive Function
# Description : Create a recursive function to calculate the factorial of a number.

user_input = int(input("Enter the number to calculate the factorial : "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(user_input))