a = 5
b = 10
print(a+b)  #Result: 15
# This is basic arithmatic operation using variables
# Now Lets try to find the area of a circle with radius 5cm
#We should always start a program with a comment addressing what the program is about

'''
    This program calculates the area of a circle
    with radius = 5cm.
    We know that the area of a circle is pi*(radius**2)
    https://en.wikipedia.org/wiki/Area_of_a_circle
    we know that:
    pi = 3.141592
    radius = 5cm
'''
pi = 3.141592
radius = 5
area = pi*(radius**2)
print("Area of the circle is:",area,"cm") #Although it works this kind of printing is very outdated

# End of Program


# We can use F'strings to format text in python 3.5 and above so,
print(f'Area of the circle is {area}cm') #this yeilds a similiar result much efficiently.
# We will stick to F'strings going ahead 

