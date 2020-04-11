'''
Finding the area of any circle.

'''

def areaOfCircle(radius):
    '''
    Computes the of circle
    Parameters: radius - numeric value
    Return Value: area - numeric value
    '''
    return 3.141593*radius**2

def main():
    r = int(input("Enter The Radius Of The Circle: "))
    print(areaOfCircle(r))

if __name__ == "__main__":
    main()
