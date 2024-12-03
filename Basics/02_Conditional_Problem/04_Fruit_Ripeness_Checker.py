# Fruit Ripeness Checker
# Description : Determine if a fruit is ripe, Overripe, or unripe based on it's color. Green -> Unripe, Yellow -> Ripe, Brown -> OverRipe

Fruit_color = input("Enter the color of the fruit ")

Fruit_color = Fruit_color.lower()

if Fruit_color == "green":
    print("Your fruit is UnRiped")
    print("Wait for Ripping the fruit")
elif Fruit_color == "yellow":
    print("Your fruit is Fully Riped")
    print("It is Ready to Eat")
elif Fruit_color == "brown":
    print("Your fruit is OverRipe")
    print("Do not eat this fruit")
else: print("Invalid color")