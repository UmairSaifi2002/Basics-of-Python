# Function with **kwargs
# Description : Create a function that accepts any number of keyword arguments and prints them in the format ket:Value

# def print_kwargs(name,power):
#     print("name: ", name ," power: ", power)

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

# print_kwargs(name = "Shaktimaan", power = "lazers")
print_kwargs(power = "lazers", name = "Shaktimaan")
