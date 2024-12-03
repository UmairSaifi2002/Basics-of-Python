# Property Decorators
# Description: Use a property decorator in the Car class to make the model attribute read-only.

class Car:

    # total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        # total_car += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand+" !"
    
    def get_model(self):
        return self.__model+" !"
    
    def fuel_type(self):
        return "Petrol and Diesel."

    @staticmethod
    def general_discription():
        return "Car is mainly powered by Petrol or Diesel."
    
    # when we create a attributes of class which is private
    # then it is both not accessible or readable
    # so using @property we can allow a private attribute of calss that objects can only read it not manipulate.
    # and @property  give us the power to access this mothod as a property
    # it means it can be read by 'my_car.model' as a property of an object.
    @property
    def model(self):
        return self.__model
    


class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def get_brand(self):
        return self.__brand+" !"
    
    def get_model(self):
        return self.__model+" !"
    
    def fuel_type(self):
        return "Petrol and Diesel."
    
    @staticmethod
    def general_discription():
        return "only Few Cars is mainly powered by Electricity."
    

my_car = Car("Tata","Nexon")

# my_car.model = "City"
print(my_car.model)