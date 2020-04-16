from some_file import my_function
from my_stupid_package import name_me, email

from urllib.error import HTTPError


# print(my_function("aviik"))

global rakhee_sawant 
rakhee_sawant = 40

y = 0

my_list = [1,2,44,56.77, 65, 5.99, "abc"]

def my_func():
    '''
    This function returns y. doc-string
    '''
    y = 5
    return y

def my_new_func():
    y = 6
    return y

def very_new_func():
    rakhee_sawant = 30
    return rakhee_sawant

print(very_new_func())

print(my_func())
print(my_new_func())
print(y)
for y in my_list:
    print(y)
print(email.my_func())