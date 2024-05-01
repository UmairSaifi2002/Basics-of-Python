import math
import time
print("Your file is here ")
username = "umair saifi"
print(username)

# >>> open('first.py')
# <_io.TextIOWrapper name='first.py' mode='r' encoding='cp1252'>
# >>> f = open('file.py')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'file.py'


# >>> f = open('first.py') 
# >>> f.readline()
# 'import math\n'

# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# 'print("Your file is here ")\n'
# >>> f.readline()
# 'username = "umair saifi"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''
# >>> f.readline()
# ''
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


# >>> f = open('first.py') 
# >>> f.__next__()
# 'import math\n'
# >>> f.__next__()
# 'import time\n'
# >>> f.__next__()
# 'print("Your file is here ")\n'
# >>> f.__next__()
# 'username = "umair saifi"\n'
# >>> f.__next__()
# 'print(username)'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# >>> for line in open('first.py')
#   File "<stdin>", line 1
#     for line in open('first.py')
#                                 ^
# SyntaxError: expected ':'


# >>> for line in open('first.py'):
# ...     print(line)
# ... 
# import math

# import time

# print("Your file is here ")

# username = "umair saifi"

# print(username)


# >>> f = open('file.py')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'file.py'


# >>> f = open('first.py') 
# >>> while True:
# ...     line = f.readline()
# ...     if not line: break
# ...     print(line)
# ... 
# import math

# import time

# print("Your file is here ")

# username = "umair saifi"

# print(username)


# >>> mylist = [1,2,3,4,5]
# >>> i = iter(mylist)
# >>> i
# <list_iterator object at 0x000002B765E5A290>
# >>> i.__next__()
# 1
# >>>
# >>> i.__next__()
# 2
# >>> i.__next__()
# 3
# >>> i.__next__()
# 4
# >>> i.__next__()
# 5
# >>> i.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


# >>> f = open('first.py')
# >>> iter(f) is f
# True
# >>> iter(f) is f.__next__()
# False


# >>>  myNewList = [1,2,3,4,5,6]
#   File "<stdin>", line 1
#     myNewList = [1,2,3,4,5,6]
# IndentationError: unexpected indent
# >>> myNewList = [1,2,3,4,5,6]  
# >>> m = iter(myNewList)
# >>> if m is iter(myNewList)
#   File "<stdin>", line 1
#     if m is iter(myNewList)
#                            ^
# SyntaxError: expected ':'
# >>> if m is iter(myNewList):
# ...     print("YES")
# ... 
# >>> m is iter(myNewList      
# ... )
# False


# >>> D = {'a':1,'b':2,'c':3}
# >>> for key in D.keys();
#   File "<stdin>", line 1
#     for key in D.keys();
#                        ^
# SyntaxError: invalid syntax
# >>> for key in D.keys();
#   File "<stdin>", line 1
#     for key in D.keys();
#                        ^
# SyntaxError: invalid syntax


# >>> for key in D.keys():
# ...     print(key)
# ... 
# a
# b
# c


# >>> i = iter(D)
# >>> i
# <dict_keyiterator object at 0x000002B765E63600>
# >>> i.__next__()
# 'a'
# >>> i.__next__()
# 'b'
# >>> i.__next__()
# 'c'
# >>>
# >>> i.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


# >>> r = range(4)
# >>> r.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'range' object has no attribute '__next__'. Did you mean: '__ne__'?


# >>> iter(r)     
# <range_iterator object at 0x000002B765AFA0B0>
# >>> r.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'range' object has no attribute '__next__'. Did you mean: '__ne__'?


# >>> i = iter(r)
# >>> i.__next__()
# 0
# >>> i.__next__()
# 1
# >>> i.__next__()
# 2
# >>> i.__next__()
# 3
# >>> i.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration