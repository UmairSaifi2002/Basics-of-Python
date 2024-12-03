integers = [1,2,3,4]
# print(integers)

stringList = ['i', 'am', 'umair', 'saifi']
# print(stringList)

mixedList = [1, 1.5, ' umair']
# print(mixedList)

nestedList = [1,2,4,[10,20,30,40],[5.7,8.9,4.2],['u','m','a','i','r'],5.678,'oiuytre']
# print(nestedList)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Accessing/Traversing the list
items = ['Milk', 'Cheese', 'Butter', 'Bread']
print(items[0])
print('Milk' in items)
print('Bun' in items)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Update/ Insert in List
myList = [1,2,3,4,5,6,7,8]
print(myList)
# update -> O(1)
myList[2] = 33 # here we update the value which present at index 2
print(myList)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Insertion
# Insert at beginning of list
# insert() function is used -> O(n)
myList.insert(0,0)
print(myList)

# Insert in middle of list -> O(n)
myList.insert(3, 44) 
print(myList)

# Insert at last of list
# append() function is used -> O(1)
myList.append(30)
print(myList)

# Insert another list to the main list 
# extend() function is used -> O(n)
newList = [121,131,141]
myList.extend(newList)
print(myList)
 
# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Slicing
mylist = ['a','b','c','d','e','f','g']
print(mylist[:]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(mylist[1:]) # ['b', 'c', 'd', 'e', 'f', 'g']
print(mylist[len(mylist):0:-1]) # ['b', 'c', 'd', 'e', 'f', 'g']
print(mylist[:2]) # ['a','b']
mylist[:2] = ['x','y'] # update the list using slicing method
print(mylist) # ['x', 'y', 'c', 'd', 'e', 'f', 'g']

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Deletion in list
# by pop() function
mylists = ['a','b','c','d','e','f','g']
print(mylists.pop()) # output -> g # it pop out & return the last index -> O(1)
print(mylists)
print(mylists.pop(2)) # output -> c # it pop out & return the third element -> O(n)
print(mylists)

# del method -> O(n)
# it delete the element without returning anything
del mylists[1]
print(mylists)

del mylists[2:4]
print(mylists)

# remove() function -> O(n)
# it use when you know which element you want to remove
mylists.remove('a')
print(mylists)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Searching in a list
ls = [10,20,30,40,50,60,70,80,90,100]
# uisng 'in' operator
# behind the scene the 'in' operator is using linear search
target = 50
if target in ls:
    print(f"The {target} is present in the given list.")
else: 
    print(f"The {target} is not present in the given list.")

# by linear search
def linear_search(lss, target):
    for i,value in enumerate(lss):
        if value == target:
            return i
    return -1

print(linear_search(ls,target))

