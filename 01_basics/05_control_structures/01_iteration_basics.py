# Lets take four inputs from the user and add them

def addFourIp(num1, num2, num3, num4):
    return num1+num2+num3+num4

def main():
    num_1 = int(input("Enter number 1: " ))
    num_2 = int(input("Enter number 2: " ))
    num_3 = int(input("Enter number 3: " ))
    num_4 = int(input("Enter number 4: " ))

    print(f'Sum is {addFourIp(num_1,num_2, num_3, num_4)}')


# so we have four inputs here so we can iterate over four numbers using a while loop


def new_main():
    count = 0
    sum = 0
    while count<4:
        num = int(input(f'Enter number {count}: '))
        sum += num
        count += 1
    return sum


'''
Computers are often used to automate repetitive tasks. 
Repeating identical or similar tasks without making errors is something that computers do well and people do poorly.

Repeated execution of a set of statements is called iteration.

An iterable is an object capable of returning its members one by one.

'''

#Basic For Loop
# Again sequences are a very common type of iterable. Some examples for built-in sequence types are lists, strings, and tuples.
# and an iterable is an object capable of returning its members one by one.



numbers = [10, 12, 15, 18, 20]   # a list is an iterable

for number in numbers:
    print(number)

# THE statement basically means 
# for iteration in iterable:
#       print(iteration)