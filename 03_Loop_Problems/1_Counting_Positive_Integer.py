# Counting Posititve Integer
# Description : Given a list of numbers, count how many are positive.
#               numbers = [1, -2, 3, -4, 5, 6 , -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6 , -7, -8, 9, 10]
positive_number_count = 0

for items in numbers :
    if items>0 :
        positive_number_count += 1

print("The Given array of numbers contains '{}' positive integers".format(positive_number_count))