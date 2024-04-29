# >>> chai_types = {"Masala":"Spicy", "Ginger":"Zesty", "Green":"Mild"} 
# >>> chai_types["Masala"]
# 'Spicy'

# >>> chai_types.get("Masala") 
# 'Spicy'

# >>> chai_types["Green"] = "Fresh"
# >>> chai_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# >>> for key in chai_types:
# ...     print(key)
# ... 
# Masala
# Ginger
# Green 


# >>> for key in chai_types:
# ...     print(key," -> ",chai_types[key] ) 
# ... 
# Masala  ->  Spicy
# Ginger  ->  Zesty
# Green  ->  Fresh 

# >>> for key,value in chai_types.items():
# ...     print(key, value)
# ... 
# Masala Spicy
# Ginger Zesty
# Green Fresh 

# >>> if "Masala" in chai_types:
# ...     print("I have Masala chai")
# ... 
# I have Masala chai

# >>> print(len(chai_types))
# 3

# >>> chai_types["Earl Grey"]="citrus"
# >>> chai_types                      
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'citrus'}

# >>> chai_types.pop("Earl Grey") 
# 'citrus'

# >>> chai_types                 
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# >>> chai_types.popitem()       
# ('Green', 'Fresh')

# >>> chai_types          
# {'Masala': 'Spicy', 'Ginger': 'Zesty'}

# >>> del chai_types["Ginger"]
# >>> chai_types
# {'Masala': 'Spicy'}

# >>> chai_types_copy = chai_types.copy()
# >>> chai_types_copy
# {'Masala': 'Spicy'}

# >>> tea_shop = {
# ... "chai":{"Masala":"Spicy","Ginger":"Zesty"},
# ... "tea":{"Green":"Mild","Black":"Strong"}
# ... }
# >>> tea_shop
# {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'tea': {'Green': 'Mild', 'Black': 'Strong'}}

# >>> tea_shop["chai"]
# {'Masala': 'Spicy', 'Ginger': 'Zesty'}

# >>> tea_shop["chai"]["Ginger"]
# 'Zesty'

# >>> squared_num = {num:num**2 for num in range(10)}
# >>> squared_num
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# >>> squared_num.clear()
# >>> squared_num
# {}

# >>> keys = ["Masala","Ginger","Lemon"]
# >>> keys
# ['Masala', 'Ginger', 'Lemon']

# >>> default_value = "Delicious"

# >>> new_dict = dict.fromkeys(keys,default_value)
# >>> new_dict
# {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

# >>> new_dict = dict.fromkeys(keys,keys)
# >>> new_dict
# {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}