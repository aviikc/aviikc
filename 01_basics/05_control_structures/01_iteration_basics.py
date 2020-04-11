# Lets take four inputs from the user and add them

def addFoueIp(num1, num2, num3, num4):
    return num1+num2+num3+num4

def main():
    num_1 = int(input("Enter number 1: " ))
    num_2 = int(input("Enter number 2: " ))
    num_3 = int(input("Enter number 3: " ))
    num_4 = int(input("Enter number 4: " ))

    print(f'Sum is {addFoueIp(num_1,num_2, num_3, num_4)}')


# so we have four inputs here so we can iterate over four numbers using a while loop


def new_main():
    count = 0
    sum = 0
    while count<4:
        num = int(input(f'Enter number {count}: '))
        sum += num
        count += 1
    return sum