# Grade Assignment
# Description : Assign a letter grade based on a student score: A(90-100), B(80-89), C(70-79), D(60-69), E(50-59), F(below 50)

student_score = int(input('Enter your score : '))

if student_score > 100:
    print("please Verify your score!")
    exit()
if 90<=student_score<=100:
    print('your Grade Score is : A')
elif 80<=student_score<=89:
    print('your Grade Score is : B')
elif 70<=student_score<=79:
    print('your Grade Score is : C')
elif 60<=student_score<=69:
    print('your Grade Score is : D')
elif 50<=student_score<=59:
    print('your Grade Score is : E')
else: print('your Grade Score is : F')
