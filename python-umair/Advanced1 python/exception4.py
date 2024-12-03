# Here we learn about the try & Catch
# exapmle 1
# try:
#     a = int(input("Enter a number : "))
#     print(a)
# except Exception as e:
#     print(e) 

# example 2
# try:
#     a = int(input("Enter the number : "))
# except ValueError as v:
#     print("Heyy, it is a ValueError")
#     print(v)
# except Exception as e:
#     print(e)

# ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# here we learn about the how we raise the error as we want

# a = int(input("Enter the First Number : "))
# b = int(input("Enter the Second Number : "))

# if b == 0:
#     raise ZeroDivisionError("Hey  our program is not meant to divide numbers by zero.")
# else:
#     print(f"The division {a}/{b} is {a/b}")

# ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# try:
#   Somecode
# except:
#   Somecode
# else:
#   Code  # This is executed only if the try was successful

# try:
#     a = int(input("Hey, Enter a number : "))
#     print(a)
# except Exception as e:
#     print(e)
# else: # This is executed only if the try was successfully executed
#     print("I am inside else.")
# finally: # Executed regardless of error! 
#     print("I am inside the finally.")

# ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# IF __NAME__== ‘__MAIN__’ IN PYTHON
# ‘__name__’ evaluates to the name of the module in python from where the program is
# ran.
# If the module is being run directly from the command line, the ‘ __name__’ is set to
# string “__main__”. Thus, this behaviour is used to check whether the module is run
# directly or imported to another file.

# yaha hame learn krna h '__name__' k bare m
# dekho agr m ek file name : first  m  function create karta hu
# aur ab dusri file : second m isse import krta hu
# to mujhe y nhi pata k y running function second file k h y first file k h
# to isiliye ham run karengy print(__name__) 
# agr to y print karta h __main__ then function current file m define h
# aur agr to y print krta h kisi file k name to y function imported h
 