x =2
y = 3
z = 4
print(x+y)
print(x**y)
print((x+y)*z)
print(40+2.23)

print(int(2.23))
print(float(40))

print('hello '+' umair')

print(x,y,z)


# >>> x=2
# >>> y=3
# >>> z=4
# >>> x,y,z
# (2, 3, 4)
# >>> x
# 2
# >>> x+1,y*2
# (3, 6)
# >>> y%2
# 1   
# >>> z**4
# 256
# >>> z**100
# 1606938044258990275541962092341162602522202993782792835301376
# >>> 100**4
# 100000000
# >>> 2**1000
# 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
# >>> result = 1/3.0
# >>> result
# 0.3333333333333333
# >>> repr('chai')
# "'chai'"
# >>> str('chai')
# 'chai'
# >>> print('chai')
# chai
# >>> 1<2
# True
# >>> 5.0 == 5.0
# True
# >>> 4.0 != 5.0
# True
# >>> x,y,z
# (2, 3, 4)
# >>> x<y<z
# True
# >>> x<y and y<z
# True
# >>> x<y or y>z
# True
# >>> 1 == 2< 3
# False
# >>> 1==2 and 2<3
# False
# >>> import math
# >>> math.floor(3.4)
# 3
# >>> math.floor(-3.4)
# -4
# >>> math.floor(3.7)  
# 3
# >>> math.floor(3.9) 
# 3
# >>> math.floor(-3.9) 
# -4
# >>> math.floor(-3.1) 
# -4
# >>> math.trunc(3.9)
# 3
# >>> math.trunc(2.9) 
# 2
# >>> math.trunc(-2.9)
# -2
# >>> math.trunc(-5.9) 
# -5
# >>> 999999999999999999999999999999 +1
# 1000000000000000000000000000000
# >>> 999999999999999999999999999999 * 100000
# 99999999999999999999999999999900000
# >>> 999999999999999999999999999999 * 100000.5433
# 1.000005433e+35
# >>> 999999999999999999999999999999 * 100000.5   
# 1.000005e+35
# >>> 999999999999999999999999999999 * 15.5     
# 1.55e+31
# >>> (2+1j)
# (2+1j)
# >>> (2+1j)*3
# (6+3j)
# >>> 0o20
# 16
# >>> 0x64
# 100
# >>> 0xFF
# 255
# >>> 0b1000
# 8
# >>> octal(64)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'octal' is not defined
# >>> oct(64)   
# '0o100'
# >>> hex(64)
# '0x40'
# >>> bin(64)
# '0b1000000'
# >>> int(3.14)
# 3
# >>> int(64,8)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: int() can't convert non-string with explicit base
# >>> int('64',8)
# 52
# >>> int('64',16) 
# 100
# >>> int('64',2)  
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 2: '64'
# >>> int('10000',2)
# 16
# >>> x =1 
# >>> x << 2
# 4
# >>> import random
# >>> random.random()
# 0.11694110921613243
# >>> random.random()
# 0.7116672849037486
# >>> random.random()
# 0.5038703092138587
# >>> random.randint(1,10)
# 4
# >>> random.randint(1,10)
# 4
# >>> random.randint(1,10)
# 3
# >>> random.randint(1,10)
# 8
# >>> random.randint(1,10)
# 7
# >>> random.randint(1,100)
# 5
# >>> random.randint(1,100)
# 34
# >>> random.randint(1,100)
# 51
# >>> l1 = ['lemon','masala','ginger','mint']
# >>> random.choice(l1)
# 'mint'
# >>> random.choice(l1)
# 'masala'
# >>>
# >>> random.choice(l1)
# 'masala'
# >>> random.choice(l1)
# 'lemon'
# >>> random.shuffle(l1)
# >>> l1
# ['masala', 'mint', 'lemon', 'ginger']
# >>> random.shuffle(l1)
# >>> l1
# ['mint', 'masala', 'lemon', 'ginger']
# >>> 0.1 + 0.1 + 0.4
# 0.6000000000000001
# >>> 0.1 + 0.1 + 0.1
# 0.30000000000000004
# >>> 0.1 + 0.1 + 0.1 - 0.3
# 5.551115123125783e-17
# >>> (0.1 + 0.1 + 0.1) - 0.3
# 5.551115123125783e-17
# >>> from decimal imporrt Decimal
#   File "<stdin>", line 1
#     from decimal imporrt Decimal
#                  ^^^^^^^
# SyntaxError: invalid syntax
# >>> from decimal import Decimal
# >>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')
# >>> from fractions import Fraction
# >>> myFraction = Fraction(2,4)
# >>> myFraction
# Fraction(1, 2)
# >>> set
# <class 'set'>
# >>> setOne = {1,2,3,4,5}
# >>> setOne & {1,2,3}
# {1, 2, 3}
# >>> setOne | {1,2,3}
# {1, 2, 3, 4, 5}
# >>> setOne | {1,2,3,7,8,6}
# {1, 2, 3, 4, 5, 6, 7, 8}
# >>> setOne - {1,2,3,4,5}6}
#   File "<stdin>", line 1
#     setOne - {1,2,3,4,5}6}
#                          ^
# SyntaxError: unmatched '}'
# >>> setOne - {1,2,3,4,5}
# set()
# >>> type(True)
# <class 'bool'>
# >>> True == 1
# True
# >>> True is 1
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# >>> False == 0
# True
# >>> False is 0
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False