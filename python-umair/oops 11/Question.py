# Ques 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
# class Programmer:
#     company: "MicroSoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin

# p = Programmer("harry", 72000, 24001)
# print(p.name, p.salary, p.pin)


# Ques 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
# import math

# class Calculator:
#     def __init__(self, num):
#         self.num = num

#     def square(self):
#         return self.num*self.num
    
#     def cube(self):
#         return self.num*self.num*self.num
    
#     def squareRoot(self):
#         return math.sqrt(self.num)

# calc = Calculator(4)
# print(calc.square())
# print(calc.cube())
# print(calc.squareRoot())


# Ques 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. 
#         Does this change the class attribute?
# class attr:
#     a = 4

# object = attr()
# object.a = 8
# print(object.a)


# Ques 4. Add a static method in problem 2, to greet the user with hello.
# import math

# class Calculator:
#     def __init__(self, num):
#         self.num = num

#     def square(self):
#         return self.num*self.num
    
#     def cube(self):
#         return self.num*self.num*self.num
    
#     def squareRoot(self):
#         return math.sqrt(self.num)

#     @staticmethod
#     def greet():
#         print("Hello Umair")

# calc = Calculator(4)
# print(calc.square())
# print(calc.cube())
# print(calc.squareRoot())


# Ques 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
# class Train:
#     ticket = 20
#     fare = 50
#     def book(self):
#         if self.ticket > 0:
#             self.ticket=self.ticket-1
#             return "You Booked a Ticket."
#         else:
#             return "All tickets are Booked."
#     def status(self):
#         return self.ticket
#     def fareInfo(self):
#         return self.fare
#
# t = Train()
# print(t.book())
# print(t.status())
# print(t.fareInfo())


# Ques 6. Can you change the self-parameter inside a class to something else (say “harry”). 
#         Try changing self to “slf” or “harry” and see the effects.
# class Class:
#     name = "class"
#     language = "python"
#     def __init__(slf, name, language):
#         slf.name = name
#         slf.language = language
#     # def __init__(harry, name, language):
#     #     harry.name = name
#     #     harry.language = language
#
# c = Class("name", "language")
# print(c.name)
# print(c.language)
