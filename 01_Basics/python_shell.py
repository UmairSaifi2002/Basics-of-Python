# PS D:\.UMAIR\Programming Languages\Basics-of-Python> cd .\01_Basics\
# PS D:\.UMAIR\Programming Languages\Basics-of-Python\01_Basics> py .\hello2_python.py
# Hello Python
# Hello umair
# Hello umair of current file
# PS D:\.UMAIR\Programming Languages\Basics-of-Python\01_Basics> ls

#     Directory: D:\.UMAIR\Programming Languages\Basics-of-Python\01_Basics


# Mode                 LastWriteTime         Length Name                                             
# ----                 -------------         ------ ----
# d-----        27-04-2024     00:07                __pycache__
# -a----        27-04-2024     00:13            450 hello2_python.py
# -a----        27-04-2024     00:01            321 hello_python.py

# PS D:\.UMAIR\Programming Languages\Basics-of-Python\01_Basics> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32   
# Type "help", "copyright", "credits" or "license" for more information.
# >>> ^D
#   File "<stdin>", line 1
#     ♦
#     ^
# SyntaxError: invalid non-printable character U+0004
# >>> ^Z

# PS D:\.UMAIR\Programming Languages\Basics-of-Python\01_Basics> python
# Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("hello umair")
# hello umair
# >>> print(34+34)
# 68
# >>> 2*2**2*2
# 16
# >>> 'umair' * 4
# 'umairumairumairumair'
# >>> name = 'umair'
# >>> print(name)
# umair
# >>> 'umair' == "umair"
# True
# >>> 'umair' === "umair"
#   File "<stdin>", line 1
#     'umair' === "umair"
#               ^
# SyntaxError: invalid syntax
# >>> import os
# >>> os.getcwd
# <built-in function getcwd>
# >>> os.getcwd()
# 'D:\\.UMAIR\\Programming Languages\\Basics-of-Python\\01_Basics'
# >>> for c in name:
# ...     print(c)
# ... ;
#   File "<stdin>", line 3
#     ;
#     ^
# SyntaxError: invalid syntax
# >>> for c in "umair":
# ...     print(c)
# ... 
# u
# m
# a
# i
# r
# >>> for c in name:
# ...     print(c)      
# ... 
# u
# m
# a
# i
# r
# >>> import sys
# >>> sys.platform
# 'win32'
# >>> import hello_python   
# Hello Python
# Hello umair
# >>> hello_python.chai("hitesh")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'hello_python' has no attribute 'chai'
# >>> hello_python.hello("hitesh") 
# Hello hitesh
# >>> from importlib import reload
# >>> reload(hello_python)
# Hello Python
# Hello umair
# <module 'hello_python' from 'D:\\.UMAIR\\Programming Languages\\Basics-of-Python\\01_Basics\\hello_python.py'>
# >>> hello_python.hello_one
# 'lemon_tea'
# >>> hello_python.hello_three
# 'masala_tea'
# >>>