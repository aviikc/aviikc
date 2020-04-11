'''
Asking user area of circle or area of rectancle to be calculated and based on
choise returning the right result.
'''
def dispalyChoices():
    print('''
            1. Area of Circle
            2. Area of Square
        ''')

def areaOfCircle(radius):
    '''
    Computes the of circle
    Parameters: radius - numeric value
    Return Value: area - numeric value
    '''
    return 3.141593*radius**2


def areaOfRect(side1, side2):
    '''
    Computes the of circle
    Parameters: radius - numeric value
    Return Value: area - numeric value
    '''
    return side1*side2


def main():
    dispalyChoices()
    choice = int(input("Enter Choice: "))
    if choice == 1:
        rad = int(input("Enter radius of circle: "))
        print(areaOfCircle(rad))
    elif choice == 2:
        side_a = int(input("Enter the length of rectancle: "))
        side_b = int(input("Enter the width of rectancle: "))
        print(areaOfRect(side_a, side_b))
    else:
        dispalyChoices()

if __name__ == "__main__":
    main()

