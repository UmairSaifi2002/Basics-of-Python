# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X 
# Ques 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.
# try:
#     with open("1.txt", 'r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("2.txt", 'r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("3.txt", 'r') as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# print("Thank you")

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X 
# Ques 2. Write a program to print third, fifth and seventh element from a list using enumerate function.
# list1 = [1,2,3,4,5,6,7,8,9,10]
# for i, item in enumerate(list1):
#     if i==3 or i==5 or i==7:
#         print(f"the value at index {i} is {item}")

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X 
# Ques 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.
# list1 = [1,2,3,4,5,6,7,8,9,10]
# num = int(input("Enter the number : "))
# table = [i*num for i in list1]
# print(table)

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X 
# Ques 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# if b == 0:
#     raise ZeroDivisionError("Infinite")
# else:
#     print(f"{a}/{b} -> {a/b}")

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X 
# Ques 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
# list1 = [1,2,3,4,5,6,7,8,9,10]
# num = int(input("Enter the number : "))
# with open('table.txt','w') as f:
#     table = [i*num for i in list1]
#     strs = ''
#     for i in table:
#         a = str(i)
#         strs = strs + a + "\n"
#     f.write(strs)


