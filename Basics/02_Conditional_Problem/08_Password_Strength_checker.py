# Password Strength Checker
# Description : Check if a password is "Weak", "Meadium", "Strong".
# Criteria : < 6 chars(Weak) , 6-10 chars(Medium), >10 chars (Strong)

password = input("Enter your Password : ")

length = len(password)
print(length)

if length < 6:
    print("Your Password is Weak.")
elif 6 <= length < 10:
    print("Your Password is Medium.")
else:
    print("Your Password is Strong.")
