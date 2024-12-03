# Prime number checker
# Description: Find out is the input given by the user is greater than zero and prime or not.

user_input = int(input("Enter your number: "))
is_prime = True

if user_input > 1:
    for i in range(2,user_input):
        if (user_input % i) == 0: 
            is_prime = False
            break
    if is_prime:
        print("{} is a prime number".format(user_input))
    else:
        print("{} is not a prime number".format(user_input))
else:
    print("Invalid input")
