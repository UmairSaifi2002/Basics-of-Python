# Transportation Mode of Selection
# Description : Choose a mode of transportation based on the distance.
# distance < 3 km -> walk, 3km < distance <= 15km -> bike,  15km < distance -> Car.

distance = int(input("Enter Distance: "))

if distance <= 3 :
    print("Your Destination is within a walking distance")
elif 3 < distance <= 15 :
    print("You can use your Bike.")
elif 15 < distance :
    print("You can use your CAR.")