# Basic Function Syntax
# Description: Write a function to calcuate and return the square of a number.

number = int(input("enter the number : "))

def square_of_num(number):
    number = number ** 2
    return number

result = square_of_num(number)
print("The square of a number {} is {}".format(number, result))
