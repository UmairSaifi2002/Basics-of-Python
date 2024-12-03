a = 89
print(f"before function call. The value of a is {a}")

def fun():
    global a
    a = 3
    print(f"Inside a function. The value of a is {a}")

fun()
print(f"after the function call. The value of a is {a}")