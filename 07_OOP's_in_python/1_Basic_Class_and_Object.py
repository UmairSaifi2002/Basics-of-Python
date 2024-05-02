# Basic Class and Object
# Description: Create a Car class with attributes like brand and model.Then create an insurence of this class

# that's how we make a class
# remember the first character of the class name have to be in Capital Letters
class Car:
    # if we want to take the argument's
    # then we define a function whic name is __init__ and self
    # see how we create this
    # __init__ is act as a constructor function which is used in javascript
    # this keyword 'self' act as 'this' keyword which is use in javaScript
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

# That's how we make an Object
my_Car = Car("Toyota","Corolla")
print(my_Car)
print(my_Car.brand)
print(my_Car.model)

my_new_car = Car("Tata","Safari")
print(my_new_car)
print(my_new_car.brand)
print(my_new_car.model)