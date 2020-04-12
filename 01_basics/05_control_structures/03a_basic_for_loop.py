'''
A for loop acts as an iterator in Python, it goes through items that are in a sequence or any other iterable item. 

Iterable items are strings, lists, tuples, dictionaries, etc

Here's the general format for a for loop in Python:

for item in object:
    statements to do stuff

The variable name used for the item is completely up to the coder, 
so use your best judgment for choosing a name that makes sense and you 
will be able to understand when revisiting your code. This item name 
can then be referenced inside you loop, for example if you wanted to 
use if statements to perform checks.

'''


l = [1,2,3,4,5,6,7,8,9,10]

for num in l:
    print(num)


for num in l:
    if num % 2 == 0:
        print(num)


for num in l:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')


# sum of items in a list
list_sum = 0 

for num in l:
    list_sum = list_sum + num

print(list_sum)