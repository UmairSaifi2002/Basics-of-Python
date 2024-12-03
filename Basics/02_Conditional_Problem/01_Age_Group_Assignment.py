# Ques 1, Age Group Assignment
# Description : Classify a person age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+)

# userAge = int(input("Enter your age: \n"))
userAge = 20

if userAge<13:
    print("You are a Child.")
elif 13<userAge<20:
    print("You are a Teenager.")
elif 20<=userAge<60:
    print("You are Adult.")
else:
    print("You are a Senior.")