# Pet Food recommandation 
# Description : Recommand a type of pet food based on the pet's species and age.
# (e.g.; Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
Pet_name = input("Enter your pet species : ")
Pet_age = int(input("Enter age of your Pet animal : "))

if Pet_age < 2 :
    food = "AI recommand you to feed Puppy {} food to your pet {}."
else:
    food = "AI recommand you to feed Senior {} food to your pet {}."

print(food.format(Pet_name,Pet_name))