# List Uniqueness Checker
# Description: Check if all elements in  a list are unique. if a duplicate is found, exit the loop and print the duplicate

list_items = ["apple", "orange", "banana", "mango", "apple"]

unique_items = set()

for item in list_items:
    if item in unique_items:
        print("Duplicate :",item)
        break
    else:
        unique_items.add(item)
