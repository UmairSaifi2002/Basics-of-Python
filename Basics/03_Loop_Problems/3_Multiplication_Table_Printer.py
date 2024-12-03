# Multiplication Table Printer
# Description : Print the multiplication table for a given number upto 10, but skip the fifth iteration.

user_input = int(input("Enter the number : "))

for num in range(1,11):
    # if num != 5 :
    #     print("{} X {} = {}".format(user_input, num, (num*user_input)))
    #     # print(user_input,'x',num,'=',user_input*num)
    # elif num == 5:
    #     print("We don't want to print this particular iteration.")

    # this is similar to above but easy and more efficient and reabable.
    if num == 5:
        print("We don't want to print this particular iteration.")
        continue
    print("{} X {} = {}".format(user_input, num, (num*user_input)))
    # print(user_input,'x',num,'=',user_input*num)