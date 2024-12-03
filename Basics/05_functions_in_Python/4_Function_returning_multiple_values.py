# Function Returning Multiple values
# Description : Create a function that returns both the area and circumference of a circle given its radius

user_input = int(input("Enter the radius of a circle : "))

def circle_area_and_circumference(radius):
    circumference = 2*3.14159*radius
    area = 3.14159*(radius**2)
    return(round(circumference,3), round(area,3))

area,circumference = circle_area_and_circumference(user_input)
print("If the radius of a circle is {} \nthen \nCircumference -> {} \nArea -> {}".format(user_input,circumference,area))