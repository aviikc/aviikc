
#built-in functions are pre defined functiond that are available in python
# example print(), input(), int(), string(), length()

name = input("Enter Name: ")
print(name)


# Eval function ised to evaluate the value of a string   ....................  important

print(eval("455"))
print(eval("12 + 45"))


# type() function values or objects in python are classified into data types of integer, float, string, list
# Python function type() tells us the type of value

print(type(12))  #Result: <class 'int'>
print(type(5.9))  #Result: <class 'float'>
print(type("Fruits"))  #Result: <class 'str'>

#Type conversion
#data types can be converted to one another. although letters cannot be converted to numbers but numbers in a string
# can be converted to integers

# lets see an example
cost_price = input("Enter Cost Price: ")
profit = input("Enter Profit: : ")
selling_price = cost_price + profit
print("Selling Price: ", selling_price) # for inputs of 100 and 50 respectively. Result: Selling Price: 10050


cost_price_new = int(input("Enter Cost Price: "))
profit_new = int(input("Enter Profit: : "))
selling_price = cost_price + profit
print("Selling Price: ", selling_price) # for inputs of 100 and 50 respectively. Result: Selling Price: 150 




# min() , max() of list
my_list = [1,2,3,4,6]

print(min(my_list))
print(max(my_list))



#importing math module  # https://docs.python.org/3/library/math.html
import math


print(math.ceil(1.4566))
print(math.floor(1.4566))

