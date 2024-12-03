# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# MAP function

# The map() function applies a given function to each item in an iterable (like a list or tuple) and returns an iterator with the results.

# Function to square a number
# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]

# # Using map to apply 'square' to each number
# squared_numbers = map(square, numbers)

# # Convert map object to a list for display
# print(list(squared_numbers))

# using lambda function
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x * x, numbers)
# print(list(squared_numbers))

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# filter() function

# The filter() function filters elements of an iterable based on a function that returns True or False.

# Function to check if a number is even
# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5]

# # Using filter to get only even numbers
# even_numbers = filter(is_even, numbers)

# print(list(even_numbers))

# using lambda function
# numbers = [1, 2, 3, 4, 5]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Reduce() function

# The reduce() function is used to apply a rolling computation to a sequence, reducing it to a single cumulative value. Unlike map and filter, it is part of the functools module and needs to be imported.

# from functools import reduce

# # Function to compute the product of two numbers
# def multiply(x, y):
#     return x * y

# numbers = [1, 2, 3, 4, 5]

# # Using reduce to compute the product of all numbers
# product = reduce(multiply, numbers)

# print(product)

# using lambda function
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)


