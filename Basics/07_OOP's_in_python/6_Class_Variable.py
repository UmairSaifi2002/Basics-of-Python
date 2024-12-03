# Class Variables
# Description : Add a class variable to Car that keeps track to the number of cars created.

class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        # this last line also done in another way
        # self.total_car += 1
        Car.total_car += 1

    def full_name(self):
        return (f"{self.__brand} {self.__model}")
    
    def get_brand(self):
        return self.__brand+" !"
    
    def get_model(self):
        return self.__model+" !"
    
    def fuel_type(self):
        return "Petrol and Diesel"
    
class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric_Charge..."


my_car = Car("Toyota","Fortuner")
my_tesla = Electric_Car("Tesla","Model S","85KWh")
safari = Car("Tata","Safari")
# test = Car("test","test")

# print(safari.total_car) -> this is not a good practice and it donot work properly
print(Car.total_car)