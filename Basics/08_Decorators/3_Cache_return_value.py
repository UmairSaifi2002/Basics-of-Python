# Cached Return Values
# Description: Implement a decorator that caches the return values of a function, 
# so that when it's called with the same arguments, the cached value is returned instead of re-executing the function

import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        return result
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(10)
    return a + b

print(long_running_func(2,5))
print(long_running_func(10,5))