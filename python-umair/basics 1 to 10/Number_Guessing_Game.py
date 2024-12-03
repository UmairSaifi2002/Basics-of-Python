import random
num = random.randint(1, 100)

a = -1

guesses = 1

while (a != num):
    a = int(input("Guess the number : "))
    if a>num :
        print("Lower Number Please")
        guesses += 1
    else:
        print("Higher Number Please")
        guesses += 1
print(f"You Guess the number {num} in {guesses} attempts")

