# Generator Function with yield.
# Description: With a generator function that yields even numbers uo to a specified limit.

limit = int(input("Enter the number : "))

# This is our Complete failure
# def even_generator(limit):
#     list_of_even_number = []
#     for i in range(2,limit+1,2):
#         list_of_even_number.append(i)
#         # print(i)

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i 
        # In layman terms, the yield keyword will turn any expression that is given with it into a generator object and return it to the caller. Therefore, you must iterate over the generator object if you wish to obtain the values stored there. we will see the yield python example.
        # Advantages of yield:
        # Using yield keyword is highly memory efficient, since the execution happens only when the caller iterates over the object.
        # As the variables states are saved, we can pause and resume from the same point, thus saving time

for i in even_generator(limit):
    print(i)
