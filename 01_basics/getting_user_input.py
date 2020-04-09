# Lets make a program to say hello to me

name = "Aviik"

print(f'Hello {name}')  #Result: Hello Aviik


# What if this is not me, what if the same program could be used by
# any individual . We then use use the input() function.

# new_name = input("Enter Your Name: ")
# print(f'Hello {new_name}!')    #Go ahead try and see what happens


'''
in the previous line of code the computer lets us type on the blinking prompt
and as soon as we press enter it prints out Hello + the new name 
'''

#Lets create a program which takes name and age of the individual and gives age in seconds.
# by that i mean if I am 1 year old it should say I am 1x365x24x60x60 seconds approximately
#Here goes the program

your_name = input("Enter Name: ")
your_age = input("Enter Age: ")

print("Hi " + your_name + ", you are  "+ your_age*365*24*60*60 + " seconds old.") #print output using any method
# print(f'Hi {your_name},you are {your_age*365*24*60*60}seconds old.')  #print output using any method ---- using F-strings
print(type(your_age))   #Result: <class 'str'>

# The input() function always saves as string.
# to convert to integer or float use int() and float() functions to do mathematical operations like.

any_number = int(input("Enter a number: "))
print(type(any_number))

#or
any_float_input_number = float(input("Enter a number: "))
print(type(any_float_input_number))