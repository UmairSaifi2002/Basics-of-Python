# Inheritance
# Description: Create an Electric Car class that inherites from the Car class and has an additional attributes battery size.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # self.brand = brand
        # self.model = model
        # these two lines are done in our Car class
        # so for this we use super keyword
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85KWh")

print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.full_name())