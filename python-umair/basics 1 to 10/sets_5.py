# Sets
# A set is an unordered, mutable collection of unique elements. 
# Sets are useful for membership testing, removing duplicates, and mathematical operations like union, intersection, etc.

# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

set = {1,2,3,4,5}
print(set) # {1,2,3,4,5}

print(len(set)) # 5

# add(value)
set.add(6)
print(set) # {1,2,3,4,5,6}

# remove(element)
print(set.remove(6)) # None
print(set) # {1,2,3,4,5}

# pop()
print(set.pop()) # 1
print(set) # {2,3,4,5}

# clear()
# set.clear() # it clear the set
# print(set)

# union(set)
set1 = {6,7,8,9,10}
union = set.union(set1)
print(union) # {2, 3, 4, 5, 6, 7, 8, 9, 10}

# intersection(set)
set2 = {3,4,5,6,7}
intersec = set.intersection(set2)
print(intersec) # {3,4,5}

#difference(set)
diff = set.difference({4,5,6,7})
print(diff) # {2,3}

# symmetric_difference(set)
sd = set.symmetric_difference({4,5,6,7})
print(sd) # {2,3,6,7}

#subset.issubset(set)
subset = {1,2}
print(subset.issubset(set))# False
print({2,3}.issubset(set))# True

#superset(set)
print(set.issuperset({2,3})) # True
print(set.issuperset({1,2,3})) # False

#disjoint() : Returns True if the two sets have no elements in common.
print(set.isdisjoint({8, 9})) # True
print(set.isdisjoint({2,3})) # False

# Ques 1 :- Write a program to input eight numbers from the user and display all the unique numbers (once).
# u = {0,}
# for i in range(8):
#     num = input(f"Enter number {i} : ")
#     u.add(int(num))
# print(u)

my_sets = {18,'18'}
print(my_sets)

s = {}
print(type(s))