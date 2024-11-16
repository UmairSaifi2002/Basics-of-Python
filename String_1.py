# In Python, strings are a type of sequence that cannot be changed once created. 
# Attempting to modify a string, such as assigning a new value to a substring or 
# using slicing to replace a portion of the string, will raise a TypeError.

# STRING is IMMUTABLE

# here we declare the string
name = "umair saifi"
print(name[:]) # -> umair saifi
print(name[0:]) # -> umair saifi
print(name[:11]) # -> umair saifi
print(name[1:6]) # -> mair
print(name[-11:-1]) # -> umair saif
print(name[1:11]) # -> mair saifi
print(name[0:11:2]) # -> uarsii

# in print statement we can inject the variable also
# we use 'f' before "" and inject the variable in {}
print(f"Good AfterNoon {name}") # -> Good AfterNoon umair saifi

letter = '''Dear, name
            You are Selected
            date '''

# let's see some function of string
# len() function -> it calculates the lenght of the string
print(len(name)) # -> 11

# endswith() -> it check the string you give is at the last
print(name.endswith('i')) # -> true
print(name.endswith('u')) # -> false

# count() -> it counts how many times a character is occur in the string
print(name.count('a')) # -> 2

# capitalize string
print(name.capitalize()) # -> Umair saifi

print(letter.replace('name','umair').replace('date','14/11/2024'))

# write a program to detect double space
str = "Hello,  Umair Saifi  you are a good boy."
print(str.find("  "))
# now replce double space to three single space
print(str.replace('  ', '   '))