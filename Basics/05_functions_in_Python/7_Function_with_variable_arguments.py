# Function with variable arguments
# Description : Write a function that takes number of arguments and returns their sum.


# Here we use '*' before the parameter it means it can take number of arguments given by the user 
# while calling this function.
# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2))
# # print(sum_all(1,2,3,4,5))
# # print(sum_all(1,2,4,5,6,7,8))

def sum_all(*chai):
    print(chai)
    # it will return a tuple of parameters
    for i in chai:
        print(i,'square is ->',i**2)
        # here wwe use a sum() which calculate a sum of the parameters
    return sum(chai)
print(sum_all(1,2))