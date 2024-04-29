# >>> tea_types = ("Black","Green","Oolong")
# >>> tea_types
# ('Black', 'Green', 'Oolong')

# >>> tea_types[0]
# 'Black'

# >>> tea_types[-1] 
# 'Oolong'

# >>> tea_types[1:]  
# ('Green', 'Oolong')

# >>> tea_types[0] = "Lemon"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# >>> len(tea_types)
# 3   

# >>> more_tea = ("Herbal","Earl Grey")
# >>> all_tea = tea_types + more_tea
# >>> all_tea
# ('Black', 'Green', 'Oolong', 'Herbal', 'Earl Grey')

# >>> if "Green" in all_tea:
# ...     print("I have Green tea")
# ... 
# I have Green tea

# >>> more_tea = ("Herbal","Earl Grey","Herbal")
# >>> more_tea.count("Herbal")
# 2   

# >>> more_tea.count("Herb")   
# 0   

# >>> (black,green,oolong) = tea_types
# >>> black
# 'Black'
# >>> green
# 'Green'
# >>> oolong
# 'Oolong'

# >>> type(tea_types)
# <class 'tuple'>