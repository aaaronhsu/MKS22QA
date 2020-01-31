from math import *

def example():
    print("This code will run")
    z = 3 + 9
    print(z)

# classwork
def circleArea():
    r = input("enter radius ")
    print(r**2 * pi)

def triangleArea():
    b = input("enter base ")
    h = input("enter height ")
    print((b * h) / 2)

def xy():
    x = input("enter x ")
    y = input("enter y ")
    print((x + y) ** 2)

def distance():
    x1 = input("enter x1 ")
    x2 = input("enter x2 ")
    y1 = input("enter y1 ")
    y2 = input("enter y2 ")
    print(sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))

# challenge
def time():
    time = input("enter time: ")
    list1 = time.split(":")
    list2 = list1[1].split(" ")

    if list2[1] == "pm":
        print(int(list1[0]) + 12, ":", list2[0], sep = '')
    else:
        print(time)
