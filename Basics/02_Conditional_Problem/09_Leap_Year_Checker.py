# Leap Year Checker
# Description: Determine if a year is a leap year.
# (Leap Year is divisible by 4, but not by 100 unless also divisible by 400).

Year = int(input("Enter the Year : "))

if Year%4 == 0:
    if Year%100 == 0:
        if Year%400 == 0:
            print("Your Year is a leap year")
        else:
            print("Your Year is not a leap year")
    else:
        print("Your Year is not a leap year")
else:
        print("Your Year is not a leap year")