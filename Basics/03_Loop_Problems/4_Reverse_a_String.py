# Reverse a String
# Description: Reverse a string using a loop.

user_input = input("Enter your String : ")


# # The Logic by me
# # Here we will find the length of our string.
# length_string = len(user_input)
# reversed_string = ''

# # Now we use the loop to Reverse the String.
# for i in range(1, length_string+1):
#     reversed_string = reversed_string + user_input[-i]

# print(reversed_string)


# By Hitesh Sir.
reversed_str = ""
for char in user_input:
    reversed_str = char + reversed_str

print(reversed_str)