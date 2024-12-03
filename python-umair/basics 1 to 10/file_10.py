# File I/O (Input/Output) in Python allows you to read from and write to files on your system. 
# Python provides a built-in open() function to work with files and several methods for interacting with file data.

# Opening file :- file = open("filename", mode)
# filename: The name of the file (can include the path).
# mode: Specifies the purpose of opening the file. Common modes:
# "r": Read (default mode). Opens the file for reading. File must exist.
# "w": Write. Creates a new file or truncates (overwrites) an existing file.
# "a": Append. Adds content to the end of the file without overwriting.
# "x": Exclusive creation. Creates a file but raises an error if it already exists.
# "b": Binary mode. Used with "rb", "wb", etc., for binary files.
# "t": Text mode (default). Used for reading/writing text files.

# Closing a file :- file.close()

# -------------------------------------------------------------------------------------------------------------------------------

# file = open("file_9.txt")
# text = file.read()
# print(text)
# file.close()

# ---------------------------------------------------------------------------------------------------------------------------------
# In order to write to a file, we first open it in write or append mode after which, 
# we use the python’s f.write() method to write to the file!
# file = open("file_9.txt","w")
# file.write("I am Fine \n What About you?")
# file.close()

# -------------------------------------------------------------------------------------------------------------------------------
# Open the file in read mode using 'with', which automatically closes the file
# with open("file_9.txt","r") as f:
#     text = f.read()
# print(text)

# -------------------------------------------------------------------------------------------------------------------------------
# readline() functoin
# with open("file_9.txt","r") as f:
#     first_line = f.readline()
# print(first_line)

# readlines() function
# with open("file_9.txt","r") as f:
#     all_lines = f.readlines()
# print(all_lines)

# write() function
# with open("file_9.txt","w") as f:
#     f.write("Hellp, Python!")

# writelines() function
# with open("file_9.txt","w") as f:
#     lines = ["Hello, Python!\n", "File I/O is easy.\n"]
#     f.writelines(lines)

# seek() function
# with open("file_9.txt", "r") as f:
#     f.seek(5)
#     print(f.read())

# tell() function
# with open("file_9.txt", "r") as f:
#     print(f.tell())

# --------------------------------------------------------------------------------------------------------------------------------
# Ques 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
# create a text file contains poem
# poem = ""
# with open("text.txt","r") as f:
#     poem = f.read()
# if str.find("twinkle"):
#   print("Twinkle is present in the poem")
# else:
#   print("Twinkle is not present in the poem")

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score.

# import random
# def game():
#   print("You are Playing the game")
#   score = random.randint(1, 62)
#   # fetch the highScore from file
#   with open("text.txt","r") as f:
#       hiscore = f.read()
#       if hiscore != "" :
#           hiscore = int(hiscore)
#       else:
#           hiscore = 0
#   print(f"Your Score: {score}")
#   if score>hiscore:
#       with open("text.txt","w") as f:
#           f.write(str(score))
#   return score
# game()

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
#         different files. Place these files in a folder for a 13 – year old.

# def generate(n):
#   table = ""
#   for i in range(1,11):
#       table += f"{n} X {i} = {n*i}\n"
#   with open(f"tables/table_{n}.txt","w") as f:
#       f.write(table) 

# for i in range(2,21):
#   generate(i)

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 4. A file contains a word “Donkey” multiple times. You need to write a program
#         which replace this word with ##### by updating the same file.

# text = ""
# with open("text.txt", "r") as f:
#     text = f.read()
#
# text = text.replace('Donkey', '#####')
# with open("text.txt","w") as f:
#     f.write(text)

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 5. Repeat program 4 for a list of such words to be censored.
# 
# words = ["Donkey", "bad", "ugly"]
# text = ""
# with open("text.txt", "r") as f:
#     text = f.read()
#
# for word in words:
#   text = text.replace(word, '#####')
# with open("text.txt","w") as f:
#     f.write(text)

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 6. Write a program to mine a log file and find out whether it contains ‘python’.
# text = ""
# with open("text.txt", "r") as f:
#     text = f.read()
# if text.find('python'):
#       print("python is present")
# else:
#      print("python is absent")

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 7. Write a program to find out the line number where python is present from ques 6.
# text = []
# with open("text.txt", "r") as f:
#     text = f.readlines()
# for i in range(len(text)):
#      if text[i].find('python):
#           print(i)

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 8. Write a program to make a copy of a text file “this. txt”
# content = ""
# with open("text.txt", "r") as f:
#      content = f.read()
# with open("Copy_text.txt", "w") as f:
#      f.write(content)

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 9. Write a program to find out whether a file is identical & matches the content of another file.
# 
# content1 = ""
# with open("text.txt", "r") as f:
#      content1 = f.read()
# content2 = ""
# with open("Copy_text.txt", "r") as f:
#      content2 = f.read()
# if content1 is content2:
#     print("Same Content")
# else: Print("Not Same Content")

# --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X --------- X ---------
# Ques 10. Write a program to wipe out the content of a file using python.
# with open("text.txt","w") as f:
#      f.write("")

