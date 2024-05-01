# Lambda Function
# Description: Create a lamda function to compute the cube of a number.

user_input = int(input("Enter the number : "))

# def lamda(number):
#     return (number**3)

# print(lamda(user_input))

cube = lambda user_input : user_input**3
print(cube)