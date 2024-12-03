# Function with multiple parameters
# Description: Create a function that takes two or more numbers as parameters and returns their sum.

num1 = int(input("Enter num1 -> "))
num2 = int(input("Enter num2 -> "))
num3 = int(input("Enter num3 -> "))

def sum(num1,num2,num3):
    return num1 + num2 + num3

print("The sum of {}, {}, and {} is-> {}".format(num1, num2, num3, sum(num1, num2, num3)))