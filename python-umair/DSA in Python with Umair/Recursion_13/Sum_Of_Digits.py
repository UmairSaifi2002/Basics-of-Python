# Find the sum of digits of a positive integer number using recursion

def SumOfDigit(n):
    if n == 0:
        return 0
    remainder = n%10
    num = int(n/10)
    return remainder+SumOfDigit(num)

print(SumOfDigit(64))

