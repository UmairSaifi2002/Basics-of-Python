# Multiple Inheritance
# Description: Create two classes Battery and Engine, and let the ElectriCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "This is a battery"

class Engine:
    def engine_info(self):
        return "This is the engine"

class ElectriCar(Battery, Engine):
    pass

my_electric_car = ElectriCar()

print(my_electric_car.battery_info())
print(my_electric_car.engine_info())