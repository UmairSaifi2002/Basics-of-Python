# Polymorphism
# Description: .nstr Demonstrate polymorphism by defining a method fuel_type in both Car
# and Electric classes, but with different behaviors

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model

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

print(my_car.fuel_type())
print(my_tesla.fuel_type())
