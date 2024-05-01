# Validate Input
# Description : Keep asking the user for input until they enter a number between 1 and 10

while True:
    number = int(input("Please enter a number between 1 and 10 : "))
    if 1<=number<=10:
        print("Thank's")
        break
    else:
        print("Invalid number, Try again.")