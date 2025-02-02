# Calculate Power of a number using recursion
def power(num, pow):
    assert int(pow) == pow, 'The power must be integer number only'
    if pow == 1:
        return num
    elif pow < 0:
        return (1/num) * power(num, pow+1)
    else: 
        return num * power(num, pow-1)

print(power(2,2))