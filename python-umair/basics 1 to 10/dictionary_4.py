# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.
my_dict = {"name": "Umair", "age": 21, "city": "Delhi", list:[1,2,3,4]}
print(my_dict["name"]) # umair

# get(key, default): Returns the value for a specified key. If the key is not found, 
# it returns the specified default value (or None if no default is provided).
print(my_dict.get("name", "unknown")) # umair
print(my_dict.get("country", "unknown")) # unknown

print(my_dict.keys()) # dict_keys(['name', 'age', 'city', <class 'list'>])
print(list(my_dict.keys())) # ['name', 'age', 'city', <class 'list'>]

print(my_dict.values()) # dict_values(['Umair', 21, 'Delhi', [1, 2, 3, 4]])
print(list(my_dict.values())) # ['Umair', 21, 'Delhi', [1, 2, 3, 4]]

print(my_dict.items()) # dict_items([('name', 'Umair'), ('age', 21), ('city', 'Delhi'), (<class 'list'>, [1, 2, 3, 4])])
print(list(my_dict.items())) # [('name', 'Umair'), ('age', 21), ('city', 'Delhi'), (<class 'list'>, [1, 2, 3, 4])]

# pop(key, default)
print(my_dict.pop(list)) # [1,2,3,4]
print(my_dict) # {'name': 'Umair', 'age': 21, 'city': 'Delhi'}

# popitem() pop the last element
city = my_dict.popitem()
print(city) # ('city', 'Delhi')
print(my_dict) # {'name': 'Umair', 'age': 21}

# clear()
print(my_dict.clear()) # None
print(my_dict) # {}

# setdefault(key, default): Returns the value of the specified key. If the key is not found, 
# it inserts the key with the specified default value and returns that value.
my_dict = {"name": "Umair"}
my_dict.setdefault("age", 25)  
print(my_dict)  # Output: {'name': 'Umair', 'age': 25}

# Ques 1 :- 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
# words = {
#     'madad' : 'help',
#     'kursi' : 'chair',
#     'billi' : 'cat'
# }

# word = input()
# print(words[word])

# Ques 1 :- Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. 
#           Assume that the names are unique.
my_dict = {}
for i in range(4):
    key = input("Enter your name : ")
    value = input("Enter your favourite language : ")
    my_dict.setdefault(key,value)
print(my_dict)
