# Question - How to check if an array contains a number

def FindNumber(ls, num):
    # return num in ls  # by inbuilt function
    # by hardcoded logic
    exist = False
    for i in ls:
        if i == num:
            exist = True
            break
    if exist:
        return f"{num} is present in the array"
    else:
        return f"{num} is not present in the array"


ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num = 16
print(FindNumber(ls, num))
