# list is muttable in nature
# Python lists are containers to store a set of values of any data type.
list = ["apple", "akash", "rohan", 7, False]
print(list)
print(list[0])
print(list[:])
print(list[::2])

# some lists methods
l1 = [2,5,3,4,67,8,34,2,0,6,8,54,32,7,8]

# sort()
l1.sort()
print(l1)

# reverse()
l1.reverse()
print(l1)

# append()
l1.append(43)
print(l1)

#insert(index,value)
l1.insert(1,101)
print(l1)

#pop(index) it uses with index, if we use it 'listname.pop()' it remove last index value
l1.pop()
print(l1)
l1.pop(1)
print(l1)

# remove(value)
l1.remove(34)
print(l1)
l1.remove(8)
print(l1)
l1.remove(8)
print(l1)
l1.remove(8)
print(l1)
# l1.remove(8)
# print(l1)

# some Questions
# ques1 Store seven fuits given by user
# t3 = []
# for i in range (7):
#     a = input()
#     t3.append(a)

# print(t3)

# q2
# t4 = []
# for i in range (6):
#     a = int(input())
#     t4.append(a)
# t4.sort()
# print(t4)

# q3
t5 = [1,3,7,9]
len = len(t5)
s = 0
for i in range(len):
    s += t5[i]

print(s)

print(sum(t5)) # sum( is a built in function )
