# # Creating a Dictionary
# my_dict = dict()
# print(my_dict) # {}
# my_dict1 = {}
# print(my_dict1) # {}
# dictionary = dict(key1='value1', key2='value2', key3='value3')
# print(dictionary) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# eng_sp = {'one':'uno', 'two':'dos', 'three':'tres'}
# print(eng_sp) # {'one': 'uno', 'two': 'dos', 'three': 'tres'}

# Time Complexity of Creating the Dictionay
# Space Complexity of Creating the Dictionary

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Cresting Dictionary from the list
# eng_sp_list = [('one','uno'), ('two','dos'), ('three','tres')]
# my_dict2 = dict(eng_sp_list)
# print(my_dict2) # {'one': 'uno', 'two': 'dos', 'three': 'tres'}

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Update / add an element to the dictionary 
# Time Complexity -> O(1)
# myDict = {'name': 'umair','age': '27', 'height': '5f9i'}
# print(myDict) # {'name': 'umair', 'age': '27', 'height': '5f9i'}
# myDict['age'] = '21'
# myDict['height'] = '5f11i'
# print(myDict) # {'name': 'umair', 'age': '27', 'height': '5f9i'}

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Traverse a Dictionary
myDict = {'name': 'umair', 'age': '21', 'height': '5f11i'}
for key in myDict:
    print(myDict[key],end=',')
print()


