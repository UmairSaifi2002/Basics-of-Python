# Find the GCD Greatest Common Divisor of two number using recursion

# GCD is the largest positive integer that divides the numbers without a remainder
# gcd(8,12) = 4

# Most Optimized approach is Euclidean Algorithm
# gcd(48,18)
# step 1 : 48/18 = 2 remainder 12
# step 2 : 18/12 = 1 remainder 6
# step 3 : 12/6 = 2 remiander 0

# so we have to code it using recursion
def GCD(num1, num2):
    if num2 == 0:
        return num1
    else: 
        remainder = num1%num2
    print(num2, remainder)
    return GCD(num2, remainder)

print(GCD(48,18))
