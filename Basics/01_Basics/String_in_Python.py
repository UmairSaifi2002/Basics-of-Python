# >>> chai = 'Masla Chai'
# >>> chai
# 'Masla Chai'

# >>> slice_chai = chai[0:6]
# >>> slice_chai
# 'Masla '

# >>> num_list = "0123456789"
# >>> num_list[:]
# '0123456789'

# >>> num_list[3:]
# '3456789'

# >>> num_list[:7]  
# '0123456'

# >>> num_list[0:7:2]
# '0246'

# >>> num_list[0:7:3] 
# '036'

# >>> print(upper(chai))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'upper' is not defined. Did you mean: 'super'?

# >>> print(chai.upper())
# MASLA CHAI

# >>> print(chai.lower()) 
# masla chai

# >>> chai  
# 'Masla Chai'
# >>> chai = "    Masala Chai   "
# >>> print(chai)
#     Masala Chai   

# >>> print(chai.strip()) 
# Masala Chai
# >>> chai = "Lemon Chai"
# >>> print(chai.replace("Lemon","Ginger"))
# Ginger Chai
# >>> chai = "Lemon, Masala, Ginger, Mint"
# >>> print(chai.split())
# ['Lemon,', 'Masala,', 'Ginger,', 'Mint']
# >>> print(chai.split(", "))
# ['Lemon', 'Masala', 'Ginger', 'Mint']
# >>> chai = "Masala Chai"
# >>> print(chai.find("chai"))
# -1
# >>> print(chai.find("Chai")) 
# 7
# >>> chai = "Masala chai chai chai"
# >>> print(chai.count("chai"))
# 3
# >>> chai_type = "Masala"
# >>> Quantity = 2
# >>> order = "I ordered {} cups of {} chai"
# >>> order
# 'I ordered {} cups of {} chai'
# >>> print(order.format(quantity, chai_type))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'quantity' is not defined. Did you mean: 'Quantity'?
# >>> print(order.format(Quantity, chai_type)) 
# I ordered 2 cups of Masala chai
# >>> chai_variety = ["lemon","Masala","Ginger"]
# >>> chai_variety
# ['lemon', 'Masala', 'Ginger']
# >>> print(" ".join(chai_variety))
# lemon Masala Ginger
# >>> print(", ".join(chai_variety)) 
# lemon, Masala, Ginger
# >>> print(" - ".join(chai_variety)) 
# lemon - Masala - Ginger
# >>> chai = "Masala Chai"
# >>> chai
# 'Masala Chai'
# >>> print(len(chai))
# 11
# >>> chai
# 'Masala Chai'
# >>> for i in chai:
# ...     print(i)
# ... 
# M
# a
# s
# a
# l
# a

# C
# h
# a
# i
# >>> chai = "He said, \"Masala chai is awesome " " 
#   File "<stdin>", line 1
#     chai = "He said, \"Masala chai is awesome " "
#                                                 ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> chai = "He said, \"Masala chai is awesome \" " 
# >>> chai
# 'He said, "Masala chai is awesome " '
# >>> chai = "MASALA \n Chai"
# >>> chai
# 'MASALA \n Chai'
# >>> print(chai)
# MASALA 
#  Chai
# >>> chai = r"Masala\nChai"
# >>> print(chai)
# Masala\nChai
# >>> chai = r"c:\user\ped\python"
# >>> chai = r"c:\user\ped\python\" 
#   File "<stdin>", line 1
#     chai = r"c:\user\ped\python\"
#            ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> chai = r"c:\\user\\ped\\python\\" 
# >>> print(chai)
# c:\\user\\ped\\python\\
# >>> chai = r"c:\user\ped\python"      
# >>> print(chai)
# c:\user\ped\python
# >>> chai = "c:\user\ped\python"  
#   File "<stdin>", line 1
#     chai = "c:\user\ped\python"
#            ^^^^^^^^^^^^^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
# >>> chai = "c:\\user\\ped\\python" 
# >>> chai 
# 'c:\\user\\ped\\python'
# >>> chai = "Masala Chai"
# >>> print("Masala" in chai)
# True
# >>> print("Masalaa" in chai)
# False
# >>>