# Find first non-repeated character
# Given a String, Find the First non-repeated character.


user_input = input("Enter your String : ")
non_repeated_character = ""

# by me
for char1 in user_input:
    count = 0
    for char2 in user_input:
        if char1 == char2:
            count = count + 1
    if count == 1:
        non_repeated_character = char1
        break

if non_repeated_character:
    print("The first non-repeated character is:", non_repeated_character)
else:
    print("No non-repeated character found.")


# by hitesh sir
# for char in user_input:
#     if user_input.count(char) == 1:
#         non_repeated_character = char
#         break

# print("The first non-repeated character in '{}' is -> '{}'".format(user_input, non_repeated_character))