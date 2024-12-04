import random

cities_name = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

# Dictionary comprehension
cities_temp = {city : random.randint(20,30) for city in cities_name}
print(cities_temp) # {'Paris': 30, 'London': 26, 'Rome': 28, 'Berlin': 27, 'Madrid': 29}

#Dictionary Comprehension using if condition
above_22 = {city : temp for city,temp in cities_temp.items() if temp > 25}
print(above_22)

