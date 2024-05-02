username = "MohdUmairSaifi"

def function():
    username = "Umair."
    print(username)

function()
print(username)

x = 99

# def function2(y):
#     z = x + y
#     return z

# result = function2(1)
# print(result)

def function3():
    global x # now any changes is done here is terated as global changes with this variable
    x = 88

function3()
print(x)

#---------------------------------------------- Closure -----------------------------------------------

def f1():
    x = 8
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()

def coder(num):
    def actual(x):
        return x ** num
    return actual

f = coder(2)
g = coder(3)

print(f(2)) # -> 4
print(g(3)) # -> 27