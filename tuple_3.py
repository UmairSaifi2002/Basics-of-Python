# tuple is a immutable list
tuple = ("apple", "akash", "rohan", 7, False)
tuple1 = (1,) # it is a tuple containing only one element

# some functions of tuple
t1 = (3,4,57,89,3,1,35)
print(t1.count(1))
print(t1)
# index(value) -> it return the index of the value
print(t1.index(57)) # 2

print(1 in t1) # True
print(100 in t1) # False

print(len(t1)) # 7

print(min(t1)) # 1
print(max(t1)) # 89

t2 = (1, 2, 3, 4)
a, b, c, d = t2
print(a ,b, c, d) # 1 2 3 4

# some questions
# ques1 
t3 = [4,0,5,20,0,0,]
print(t3.count(0))
