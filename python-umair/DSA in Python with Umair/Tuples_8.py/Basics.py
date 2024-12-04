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
