def capitalizeFirst(arr):
    ans = arr[0]
    if not ans[0].isupper():
        a = arr[0].capitalize()
        # print(a)
        arr.pop(0)
        arr.append(a)
        return capitalizeFirst(arr)
    else:
        return arr

def capitalizeWords(arr):
    # TODO
    ans = arr[0]
    if not ans[0].isupper():
        a = arr[0].upper()
        # print(a)
        arr.pop(0)
        arr.append(a)
        return capitalizeWords(arr)
    else:
        return arr
    
print(capitalizeFirst(['car', 'banana', 'taco']))    
print(capitalizeWords(['car', 'banana', 'taco']))
