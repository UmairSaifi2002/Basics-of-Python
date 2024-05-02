# Encapsulation
# Description : Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self,brand,model):
        # to make the attributes private we have to add '__' before the variable names
        self.__brand = brand
        self.__model = model

    # now we create a getter method
    def get_brand(self):
        return self.__brand + " !"
    
    def get_model(self):
        return self.__model + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85KWh")

print(my_tesla.get_brand())
