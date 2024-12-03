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
    
    # now we create a setter method
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85KWh")

print(my_tesla.get_brand())

my_car = Car("Toyota","Corolla")
print(my_car.full_name())
my_car.set_brand("Mahindra")
my_car.set_model("TUV500")
print(my_car.full_name())