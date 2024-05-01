# Factorial Calculator
# Description : Compute the factorial of a number using a while loop.

user_input = int(input("Enter your number: "))
number = user_input
factorial = 1

while user_input > 0:
    factorial = factorial * user_input
    user_input = user_input - 1

print("The factorial of a number {} is -> {}".format(number, factorial))