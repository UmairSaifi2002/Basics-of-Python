# Coffee Customization
# Customize a coffee order : "Small", "Medium", "Large" with an option for "Extra shot" of espresso.

coffee = input("Let us Know the Quantity of a Coffee that you need : ")
extra_shot = input("do you need Extra_shot Y/N: ")

coffee = coffee.lower()
extra_shot = extra_shot.lower()

if extra_shot == "y":
    shots = "with Extra_Shot"
elif extra_shot == "n":
    shots = "without Extra_Shot"

if coffee == "small" :
    quantity = "Small"
elif coffee == "medium" :
    quantity = "Medium"
elif coffee == "large" :
    quantity = "Large"
else : 
    print("Invalid Quantity")
    exit()

order = "You Odered A {} coffee {}."
print(order.format(quantity,shots))