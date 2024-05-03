# Class Inheritance and isinstance() Function
# Description: Deminstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car():
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand+" !"
    
    def get_model(self):
        return self.__model+" !"
    
    # now we create a setter method
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model
    
    def fuel_type(self):
        return "Petrol and diesel."
    
    @staticmethod
    def general_description():
        return "Mostly Car's are powered by Petrol and diesel."
    
    @property
    def model(self):
        return self.__model
    
class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.__battery_size = battery_size

    def fuel_type(self):
        return f"Electric Charge {self.__battery_size}"
    
    @staticmethod
    def general_description():
        return "Fewer Car's are powered by Electric Charge."

    
my_tesla = Electric_Car("Tesla","Model S","85KWh")
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.get_model())
# print(my_tesla.fuel_type())
# print(my_tesla.general_description())

my_car = Car("Tata","Nexon")
# print(my_car.general_description())

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,Electric_Car))