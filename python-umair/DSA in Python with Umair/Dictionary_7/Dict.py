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
# Time Complexity -> O(1) aceessing the value from dictionary is at constant time
# myDict = {'name': 'umair','age': '27', 'height': '5f9i'}
# print(myDict) # {'name': 'umair', 'age': '27', 'height': '5f9i'}
# myDict['age'] = '21'
# myDict['height'] = '5f11i'
# print(myDict) # {'name': 'umair', 'age': '27', 'height': '5f9i'}

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Traverse a Dictionary 
# Time complexity -> O(n)
# myDict = {'name': 'umair', 'age': '21', 'height': '5f11i'}
# for key in myDict:
#     print(myDict[key],end=',')
# print()

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Linear Search in Dictionary
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}

# def search(dict, value): # Time complexity -> O(n)
#     for key in dict:
#         if dict[key] == value:
#             return f"{key} -> {value}"
#     return "Value is not Exist in Dictionary."

# print(search(myDict,'70kg')) # weight -> 70kg
# print(search(myDict,'22')) # Value is not Exist in Dictionary.


# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Delete an element from the Dictionary
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}

# pop() Time Complexity -> O(1)
# removedValue = myDict.pop('skinTone')
# print(removedValue) # fair
# print(myDict) # {'name': 'umair', 'age': '21', 'height': '5f11i', 'weight': '70kg', 'country': 'India'}

# remove = myDict.pop('nam', 'None') # if key is not present in the Dictionary so it return the default value 
# print(remove) # None

# # popitem() -> it return the last key value pair
# # Time Complexity -> O(1)
# pair = myDict.popitem()
# print(pair) # ('country', 'India')
# print(type(pair)) # <class 'tuple'>

# # clear() -> it delete whole the dictionary
# # Time Complexity -> O(n)
# myDict.clear()
# print(myDict) # {}

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# copy() - it gies the shallow copy
# means it donot modify the original dictionary
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# copyDict = myDict.copy()
# print(myDict == copyDict)
# copyDict['age'] = '20'
# print(myDict == copyDict)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# fromkeys(sequence of keys[], default value) -> The .fromkeys() method returns a dictionary with a specified set of keys. It can also initialize the entries with a specified value.
# newDict = {}.fromkeys([1,2,3,4,5,6],0) # here we give 0 as a default value of all the keys
# print(newDict) # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# neewDict = {}.fromkeys([1,2,3]) # if we use it without the default value then the value is None
# print(neewDict) # {1: None, 2: None, 3: None}

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# get(key, value-> gives default value to non existed key)
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# print(myDict.get('name')) # umair
# print(myDict.get('nam','Not Exist')) # Not Exist

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# items() -> it return the key, value pair as a list
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# print(myDict.items()) # dict_items([('name', 'umair'), ('age', '21'), ('height', '5f11i'), ('weight', '70kg'), ('skinTone', 'fair'), ('country', 'India')])

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# keys() -> it return the list of keys
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# print(myDict.keys()) # dict_keys(['name', 'age', 'height', 'weight', 'skinTone', 'country'])

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# popitem() -> it delete & return the last pair
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# print(myDict.popitem()) # ('country', 'India')

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# setdefault(key, defaultvalue) -> it return the value if key present in the dictionary from the dictionary 
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# print(myDict.setdefault('name'))
# print(myDict.setdefault('number','80******39')) # if key is not present in the dictionary so it set the key and value in the dictionary
# print(myDict)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# value() -> it return the list of values of the dictionary
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# print(myDict.values()) # dict_values(['umair', '21', '5f11i', '70kg', 'fair', 'India'])

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # update() -> it update the key value pairs
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# myDict.update({'name':'Umair Saifi'}) # it update the value of the existed key
# print(myDict) # {'name': 'Umair Saifi', 'age': '21', 'height': '5f11i', 'weight': '70kg', 'skinTone': 'fair', 'country': 'India'}
# myDict.update({'Student':'Yes'}) # if the key is not exists in dictionary then it add as new Key,Value Pair
# print(myDict) # {'name': 'Umair Saifi', 'age': '21', 'height': '5f11i', 'weight': '70kg', 'skinTone': 'fair', 'country': 'India', 'Student': 'Yes'}

# -----------------------------------------  Built in Function  -----------------------------------------
# 'in' operator
# this operator help us to check the key present in dictionary or not
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# print('name' in myDict) # True
# print('umair' in myDict.values()) # True
# print('Umair' in myDict) # False

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# not operator
# myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
# print('name' not in myDict) # False
# print('Umair' not in myDict.values()) # True

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# len() function gives the length of the dictionary
myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
print(len(myDict)) # 6

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# sorted() function -> it sort the dictionary
myDict = {'name':'umair', 'age':'21', 'height':'5f11i', 'weight':'70kg', 'skinTone':'fair', 'country':'India'}
print(sorted(myDict)) # ['age', 'country', 'height', 'name', 'skinTone', 'weight']


