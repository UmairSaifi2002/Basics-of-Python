# Timming Function Execution
# Description: Write a decorator that measures the time a function takes to execute

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}secs")
        return result
    return wrapper


# ham jo bhi naam likhty h @ laga kr to vo decorator hota h
# aur jis nhi function k uper ham decorator likhty h y lagaty h to
# vo function directly call nhi hog
# pehle vo dusra function run hoga jiska naam decorator m likha hua h
# phir vo run hoga
@timer
def example_function(n):
    time.sleep(n)

example_function(2)