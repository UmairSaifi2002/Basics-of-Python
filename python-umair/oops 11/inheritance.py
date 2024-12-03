# Inheritance is a way of creating a new class from an existing class.
# single inheritance
# class Company:
#     comp_name = "ASUT pvt ltd"

# class Employee(Company):
#     e_name = "umair"
#     position = "Head"

# a = Company()
# print(a.comp_name)

# b = Employee()
# print(b.comp_name)
# print(b.e_name)
# print(b.position)

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------

# Multiple inheritance
# class Employee:
#     company = "ASUT"
#     name = "name"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the company is {self.company}")
    
# class coder:
#     language = "Python"
#     def printlanguage(self):
#         print(f"Out of all the language here is your language {self.language}")

# class Programmer(Employee, coder):
#     company = "HCL"
#     def showLanguage(self):
#         print(f"The name is {self.name} an he is good with {self.language} language.")

# a = Programmer()
# a.show()
# a.printlanguage()
# a.showLanguage()

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------

# Multi-Level Inheritance
# When a child class becomes a parent for another child class.
# class Employee:
#     a = 1
# class Programmer(Employee):
#     b = 2
# class Manager(Programmer):
#     c = 3

# m = Manager()
# print(m.a)
# print(m.b)
# print(m.c)

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------

# use of 'super' Keyword
# super() method is used to access the methods of a super class in the derived class.
# derived class can access the constructor of its parent class by using 'super' keyword

# class Employee:
#     name = "employee"
#     def __init__(self):
#         print("Constructor of Employee.")

# class Programmer(Employee):  # Inherit from Employee
#     name = "programmer"
#     def __init__(self):
#         super().__init__()  # Call Employee's constructor
#         print("Constructor of Programmer.")

# class Manager(Programmer):  # Inherit from Employee
#     name = "Manager"
#     def __init__(self):
#         super().__init__()  # Call Employee's constructor
#         print("Constructor of Manager.")

# # Testing
# a = Employee()
# print(a.name)  # Output: Constructor of Employee. | employee

# b = Programmer()
# print(b.name)  # Output: Constructor of Employee. | Constructor of Programmer. | programmer

# c = Manager()
# print(c.name)  # Output: Constructor of Employee. | Constructor of Manager. | Manager

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The class attribute 'using @classmethod' of a is {cls.a}")

# class program:
#     programLine = 30
#     def showLine(self):
#         print(f"The class attribute will change without '@classmethod' so, programLine {self.programLine}")

# a = Employee()
# a.a = 5
# a.show()

# b = program()
# b.showLine()

# b.programLine = 35
# b.showLine()

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------

# class Employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"The class attribute 'using @classmethod' of a is {cls.a}")

#     # here function name work as an attribute because of '@property' method
#     @property
#     def name(self):
#         return f"{self.fname}, {self.lname}"
    
#     # here a function sets the name in a pattern 
#     # means a function is there to perform on a function
#     @name.setter
#     def name(self, value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# in above the class we perform a function's for the name
# and our user is not aware of it so, we perform function on data without the awarness of user
# this is called 'Abstraction'

# and we collect all the method in a single unit
# means we encapsulate the function in a single unit
# this is 'Encapsulation'

# e = Employee()
# e.a = 45

# e.name = "Umair Saifi"
# print(e.name)
# print(e.fname)
# print(e.lname)

# e.show()

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         # Define custom addition for Point objects
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         # Custom string representation for printing
#         return f"({self.x}, {self.y})"

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2  # Calls __add__

# print(p3)  # Output: (4, 6)

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------


