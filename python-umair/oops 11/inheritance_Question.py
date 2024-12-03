# Ques 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
# class TwoDVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

# class ThreeDVector(TwoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k

# two = TwoDVector(1,2)
# three = ThreeDVector(11,22,33)
# print(two.i, two.j)
# print(three.i, three.j , three.k)

# -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X --------
# Ques 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. 
#         Add a method ‘bark’ to class ‘Dog’. 
# class Animal:
#     def __init__(self):
#         print("animal constructor.")
    
# class Pets(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Pets constructor.")

# class Dog(Pets):
#     def __init__(self):
#         super().__init__()
#         print("Dog constructor.")
#     def bark(self):
#         print("Dog always barks")

# a = Animal()
# p = Pets()
# d = Dog()
# d.bark()

# -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X --------
# Ques 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary.

# class Employee:
#     salary = 234
#     increment = 10

#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#          self.increment = ((salary/self.salary)-1)*100

# e = Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 290.16
# print(e.increment)

# -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X --------
# Ques 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ 
# which adds and multiplies them.

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i
#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
#     def __str__(self):
#         return f"The Complex Number is : {self.r} + {self.i}i"

# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1+c2)

# -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X -------- X --------
# Ques 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = Vector(7,8,9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)
