# Ques 1. Write a program to find the greatest of four numbers entered by the user.
# first = int(input("Enter First number : "))
# second = int(input("Enter Second number : "))
# third = int(input("Enter Third number : "))
# fourth = int(input("Enter Fourth number : "))

# if (first > second):
#     # first > second
#     if(first > third):
#         # first > third
#         if(first > fourth):
#             # first is the greatest
#             print(first)
#         else: 
#             # first < fourth
#             print(fourth)
#     else: 
#         # first < third
#         if(third > fourth):
#             # third is greatest
#             print(third)
#         else:
#             # fourth is greatest
#             print(fourth)
# else: 
#     # first < second
#     if(second > third):
#         # second > third
#         if(second > fourth): 
#             # second is greatest
#             print(second)  # Fixed here
#         else: 
#             # second < fourth
#             print(fourth)
#     else: 
#         # second < third
#         if(third > fourth):
#             # third is greatest
#             print(third)
#         else: 
#             # fourth is greatest
#             print(fourth)

# -------------------------------------------------------------------------------------------------------------------

# Ques 2 :- Write a program to find out whether a student has passed or failed if it requires a
#           total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
#           take marks as an input from the user.

# Math_marks = int(input("Enter your Maths marks : "))
# Science_marks = int(input("Enter your Science marks : "))
# IT_marks = int(input("Enter your IT marks : "))

# first_Check = 100/3
# second_Check = 100/2.5

# total = Math_marks + Science_marks + IT_marks

# if((Math_marks >= first_Check) & (Science_marks >= first_Check) & (IT_marks >= first_Check)):
#     if(total >= second_Check):
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Fail")

# -------------------------------------------------------------------------------------------------------------------

# Ques 3 :- A spam comment is defined as a text containing following keywords:
#           “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
#           to detect these spams.

# text = input("Enter the Comment : ")
# if(("Make a lot of money" in text) or ("buy now" in text) or ("subscribe this" in text) or ("click this" in text)):
#     print("Spam Comment is Detected")
# else: 
#     print("Normal Comment")

# -------------------------------------------------------------------------------------------------------------------

# Ques 4 :- Write a program to find whether a given username contains less than 10 characters or not.
# user_name = input("Enter the UserName : ")
# if(len(user_name) > 10):
#     print("UserName contains greater than 10 character.")
# elif(len(user_name) == 10):
#     print("UserName have 10 Character.")
# else:
#     print("Username contains less than 10 character.")

# -------------------------------------------------------------------------------------------------------------------

# Ques 5 :- Write a program which finds out whether a given name is present in a list or not.
# names = ['u', 'm', 'a', 'i', 'r']
# name = input("Enter your name: ")

# if name in names:
#     print("Your name is present in the list.")
# else:
#     print("Your name is not present in the list.")

# -------------------------------------------------------------------------------------------------------------------

# Ques 6 :- Write a program to calculate the grade of a student from his marks from the
#           following scheme:
#           90 – 100 => Ex
#           80 – 90 => A
#           70 – 80 => B
#           60 – 70 =>C
#           50 – 60 => D
#           <50 => F

# grade = int(input("Enter your grade : "))
# if(100 >= grade > 90):
#     print("Ex")
# elif(90>= grade > 80):
#     print("A")
# elif(80>= grade > 70):
#     print("B")
# elif(70>= grade > 60):
#     print("C")
# elif(60>= grade > 50):
#     print("D")
# else:
#     print("F")

# -------------------------------------------------------------------------------------------------------------------

# Ques 7 :- Write a program to find out whether a given post is talking about “Harry” or not.
post = input()
if("Harry" in post):
    print("Given post is talking about \"Harry\"")
else:
    print("Given post is NOT talking about \"Harry\"")