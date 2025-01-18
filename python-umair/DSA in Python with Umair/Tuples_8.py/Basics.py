tuple1 = ('a','b','c','d')
print(tuple1)

tuple2 = ('a',)
print(tuple2)

# traversing a tuple 
t = (1,2,3,4,5,6,7,8)
for i in t:
    print(i,end=', ')
print()
for i in range(len(t)):
    print(i,end=', ')
print()

# Search in a tuple
newTuple = ('a','b','c','d','e')
print(newTuple.index('b'))
# searching using the for loop
def searchElement(tuple, element):
    for i in range(len(tuple)):
        if tuple[i] == element:
            return f"Element {element} is present at index : {i}"
    return f"Element {element} is not present in Tuple."
print(searchElement(newTuple,'f'))

# Tuple Operation / Function
tup1 = (1,2,3,4)
tup2 = (5,6,7,8)
add = tup1 + tup2
print(add) # (1,2,3,4,5,6,7,8)
print(tup1*4)

# in operator
print(4 in tup1)
print(5 in tup1)

# count() operator it counts the occurence of the number in a tuple
print(tup1.count(2))

# len() function it return the length of the tuple
print(len(add))

# max() function
print(max(tup2))

# we can convert the list to tuple 
tup = tuple([1,2,3,4])
print(type(tup))

tupl = tuple(['a','b','c','d'])
print(tupl)

