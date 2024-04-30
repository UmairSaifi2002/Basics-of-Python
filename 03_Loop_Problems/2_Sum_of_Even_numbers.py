# Sum of Even Numbers
# Description: Calcuate the sum of even numbers up to a given number n.

number = int(input("Enter the number : "))

sum = 0

# if we want to iterate over the number
# we known that 'int' is an Object which is not iterable
# so we use a keyword 'range(start,end)' function. end is not included

# here is the code known analyse it carefully.
for num in range(1,number+1):
    if num%2 == 0:
        sum += num

print("If the range is belongs to {} - {}\nThe sum of even numbers is -> {}".format(0,number,sum))