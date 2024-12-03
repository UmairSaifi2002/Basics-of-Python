# Default Parameter Value
# Description : Write a function that greets a user. if no name is provided, it should greet with a default name.

def greeting(name = 'user'):
    return "Hello Good Morning {}".format(name)

print(greeting())
print(greeting('umair'))