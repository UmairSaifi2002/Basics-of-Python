# weather Activity Suggestion
# Description: Suggest an activity based on the weather
# Sunny -> Go for a walk, Rainy -> Read a Book, Snowy -> Build a SnowMan

weather = input("Enter your current weather condition in LowerCase : ")

weather = weather.lower()

if weather == "sunny":
    print("You can Go for a Walk.")
elif weather == "rainy":
    print("Stay Home and Enjoying while Reading a Book.")
elif weather == "snowy":
    print("You can Go Outside and Build a Snowman.")
else: print("Please enter a valid weather condition")