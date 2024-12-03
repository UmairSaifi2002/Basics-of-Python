# Ques 2, Movie Ticket Pricing.
# Description : Movie Ticket Priced based on Age: $12 for adults (18 and over), $8 Cildren. EveryOne gets a $2 Discount on Wednesday.

userAge = int(input("Enter your age for pricing: \n"))
day = input("Enter day name: \n")
day = day.lower()
price = 0

if userAge>=18: price = 12
else: price = 8

if day == "wednesday":
    price = price - 2
    print("Your Ticket price is : ",price)
else: print("Your Ticket price is : ",price)