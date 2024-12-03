# # List Operators & functions
# l = [1,2,3,4,5,6]
# s = [7,8,9,10]
# ls = l + s # Concatenation - it add the list together
# print(ls)

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # '*' operator
# a = [1,2]
# a = a * 4
# print(a)

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # len() function -> to count the number of elements in the list
# print(len(ls)) # output -> 10

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # max() function - it return the maximum element form the list
# print(max(ls)) # output -> 10
# # min() function - it return the minimum element form the list
# print(min(ls)) # output -> 1

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # sum() function - it return the sum of the all elements of the given array
# print(sum(ls)) # output -> 55

# # Question - find the average of given list
# Sum = sum(ls)
# lenght = len(ls) 
# average = Sum / lenght
# print(average) # output -> 5.5

# # challenge - ReWrite this code by using list operations
# # total = 0
# # count = 0
# # while True:
# #     inp = input('Enter the number : ')
# #     if inp == 'done' or inp == 'Done':
# #         break
# #     value = float(inp)
# #     total = total + value
# #     count = count + 1
# #     average = total / count
# # print(f'Average :  {average} ')

# # Challenge Completed!!
# # def average(lists):
# #     Sum = sum(lists)
# #     Len = len(lists)
# #     return Sum/Len

# # lists = []

# # while True:
# #     val = input('Enter the value : ')
# #     if val == 'done' or val == 'Done':
# #         break
# #     lists.append(int(val))

# # print(average(lists))

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# # Convert string to list
a = 'spam'
b = list(a)
print(b) # ['s', 'p', 'a', 'm']

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
name = 'Mohd Umair Saifi'
# using split() function it split the string and convert into list
# syntax stringName.split(delimintor)
# deliinator is a notation on the basis of which we split our string 
# by default it is ' '
ls = name.split()
print(ls) # ['Mohd', 'Umair', 'Saifi']

c = 'spam0-spam1-spam2'
d = c.split('-')
print(d) # ['spam0', 'spam1', 'spam2']

# if we want to convert the list to string we uses 'join()' function
# syntax deliminator.join(listName)
deliminator = '-'
e = deliminator.join(d)
print(e) # spam0-spam1-spam2

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# list comprehension

array_list = [1,2,3,4]
new_list = [i*2 for i in array_list]
print(new_list) # [2, 4, 6, 8]

language = 'Python'
langList = [i for i in language]
print(langList) # ['P', 'y', 't', 'h', 'o', 'n']

# lists comprehension with if-else condition
number = [1,2,3-1,4,-4,-6,5,8,7]
positive_number = [i for i in number if i>0]
print(positive_number) # [1, 2, 2, 4, 5, 8, 7]

negative_number = [i for i in number if i<0]
print(negative_number) # [-4, -6]

negative_number_square = [i*i for i in number if i<0]
print(negative_number_square) # [16, 36]

# # Q - Write a code for checking a word contains Consonent
sentence = 'my name is umair'
def is_consonent(word):
    vowels = 'aeiou'
    return word.isalpha() and word.lower() not in vowels
consoSen = [i for i in sentence if is_consonent(i)]
print(consoSen)
sc = ''.join(consoSen)
print(sc)

# another pattern of list comprehension using if else
numbers = [1, 10, -10, -4, -5, 3, 22, 76, -9, 43]
pos_num = [num if num > 0 else 0 for num in numbers]
print(pos_num)
neg_numm = [num if num< 0 else 0 for num in numbers]
print(neg_numm)

