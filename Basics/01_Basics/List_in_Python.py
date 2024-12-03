# >>> tea_varities = ["Black","Green","Oolong","White"]  
# >>> tea_varities
# ['Black', 'Green', 'Oolong', 'White']
# >>> print(tea_varities) 
# ['Black', 'Green', 'Oolong', 'White']

# >>> print(tea_varities[-1])
# White

# >>> print(tea_varities[1:3])  
# ['Green', 'Oolong']

# >>> print(tea_varities[:3])  
# ['Black', 'Green', 'Oolong']

# >>> print(tea_varities[:2]) 
# ['Black', 'Green']

# >>> print(tea_varities[2:])  
# ['Oolong', 'White']

# >>> tea_varities[3]
# 'White'

# >>> tea_varities[3] = "Harbel"
# >>> tea_varities              
# ['Black', 'Green', 'Oolong', 'Harbel']

# >>> tea_varities[1:2]
# ['Green']

# >>> tea_varities[1:2] = "Lemon"
# >>> tea_varities               
# ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Harbel']

# >>> tea_varities[1:2] = ["Lemon"] 
# >>> tea_varities
# ['Black', 'Lemon', 'e', 'm', 'o', 'n', 'Oolong', 'Harbel']

# >>> tea_varities = ["Black","Green","Oolong","White"]
# >>> tea_varities[1:2] = ["Lemon"]
# >>> tea_varities                 
# ['Black', 'Lemon', 'Oolong', 'White']

# >>> tea_varities[1:3] = ["Green","Masala"]  
# >>> tea_varities                           
# ['Black', 'Green', 'Masala', 'White']

# >>> tea_varities[1:1]
# []

# >>> tea_varities[1:1] = ["New-Chai","Old-Delhi-Chai"]
# >>> tea_varities
# ['Black', 'New-Chai', 'Old-Delhi-Chai', 'Green', 'Masala', 'White']    

# >>> tea_varities[1:2]
# ['New-Chai']

# >>> tea_varities[1:3]
# ['New-Chai', 'Old-Delhi-Chai']

# >>> tea_varities[1:3] = []
# >>> tea_varities
# ['Black', 'Green', 'Masala', 'White']

# >>> for chai in tea_varities:
# ...     print(chai)
# ...
# Black
# Green
# Masala
# White

# >>> for chai in tea_varities:
# ...     print(chai,end=" ")
# ...
# Black Green Masala White >>>

# >>> tea_varities
# ['Black', 'Green', 'Masala', 'White']
# >>> if "Oolong" in tea_varities:
# ...     print("I have Oolong tea")
# ...

# >>> tea_varities.append("Oolong")
# >>> if "Oolong" in tea_varities:")
# ...     print("I have Oolong tea")
# ...
# I have Oolong tea

# >>> tea_varities                 )
# ['Black', 'Green', 'Masala', 'White', 'Oolong']

# >>> tea_varities.pop()
# 'Oolong'
# >>> tea_varities
# ['Black', 'Green', 'Masala', 'White']

# >>> tea_varities.remove("Green")
# >>> tea_varities
# ['Black', 'Masala', 'White']

# >>> tea_varities.insert(1,"Green")
# >>> tea_varities
# ['Black', 'Green', 'Masala', 'White']

# >>> tea_varities_copy = tea_varities.copy()
# >>> tea_varities_copy
# ['Black', 'Green', 'Masala', 'White']

# >>> tea_varities_copy.append("Lemon")
# >>> tea_varities_copy
# ['Black', 'Green', 'Masala', 'White', 'Lemon']
# >>> tea_varities
# ['Black', 'Green', 'Masala', 'White']

# >>> squared_nums = [x**2 for x in range(10) ]
# >>> squared_nums
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# >>> cube_num = [y**3 for y in range(5)]
# >>> cube_num
# [0, 1, 8, 27, 64]