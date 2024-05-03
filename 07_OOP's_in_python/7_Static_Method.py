# Static Method -> it is a method which is only accessed by class not by objects.
# Description: Add a static method to the Car class that returns a general description of a car.

# @staticmethod is a decorator which enhances the function of the methods

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand+" !"
    
    def get_model(self):
        return self.__model+" !"
    
    def fuel_type(self):
        return "Petrol and Diesel"
    
    # here we create this function a static method
    @staticmethod # now general_description is a static method
    # and we are removing this self from its parameter.
    def general_discription():
        return "Cars are means of Transport. and its fuel is Petrol and Diesel."
    
class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.__battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge..."
    
    # here we create this function a static method
    @staticmethod # now general_description is a static method
    # and we are removing this self from its parameter.
    def general_discription():
        return "Cars are means of Transport. and its fuel is Electricity."
    
my_car = Car("Toyota","Fortuner")
my_tesla = Electric_Car("Tesla","Model S","85KWh")
safari = Car("Tata","Safari")

# my_car1 = my_car.general_discription()
# print(my_car.general_discription()) # here we access this by object

# here we access this by class
# wait you have to make some changes to access this function by class
# first step -> You have to make it static method
# second step -> remove 'self' from its parameter
# third step -> access this by class
print(Car.general_discription()) 

# Same as above
# my_tesla1 = my_tesla.general_discription()
# print(my_tesla.general_discription()) 
print(Electric_Car.general_discription())
