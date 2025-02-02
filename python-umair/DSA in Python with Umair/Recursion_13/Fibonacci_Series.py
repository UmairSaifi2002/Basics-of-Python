# Here we will learn to code a Fibonacci Series

def fibonacci(n):
    # Base Case's
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) # Recursive Call

# for a single number
a = fibonacci(6)
print(a)

# To print the sequence
for i in range(10):
    a = fibonacci(i)
    print(a,end=', ')