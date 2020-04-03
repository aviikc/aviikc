#1,2,3,4,5,........454, -23,-56, 567, .....54..... all these are INTEGERS.
#12.4, -4.6, 6.89, 34.789834, .00000034, -.0002, 0.00024 .... all these are FLOATS.
#A string is written between two "" or ''. "This is a string.", "1,2,4,4,6,78" is a string.
#These are three main data types in python.

# You can add between integers and floats
print(1 + 1.5)

# you can substract also
print(1 - 1.5)

# you can multiply also ...... 
print(1*1.5)
# see the result is a float

# division is a bit tricky so be CAREFUL
print(5/2)  # This is supposed to give 2.5
# Python 3.5 is good and does the conversion automatically
# Previous versions might need 
print(5/2.0) #or
print(5.0/2) #or
print((5*1.0)/2) # and so on......
# Please Remember this as its important for exams and in Houdini as VEX language does not
# convert to float as easily as Python does. 