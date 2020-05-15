import turtle
import random

# classwork/homework
def triangle(t1):
    for i in range(3):
        t1.forward(50)
        t1.right(120)

def circle(t1):
    t1.circle(50)

def square(t1):
    for i in range(4):
        t1.forward(50)
        t1.right(90)

def pentagon(t1):
    for i in range(5):
        t1.forward(50)
        t1.right(72)

def star(t1):
    for i in range(5):
        t1.forward(50)
        t1.right(144)

def shapes():
    t1 = turtle.Turtle()
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.setup(width = 1000, height = 1000)
    turtle.colormode(255)
    t1.pu()

    for i in range(100):
        t1.begin_fill()
        t1.goto(random.randint(-450, 450), random.randint(-450, 450))
        t1.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        choice = random.randint(0, 4)
        print(choice)
        t1.begin_fill()
        if choice == 0:
            triangle(t1)
        elif choice == 1:
            circle(t1)
        elif choice == 2:
            square(t1)
        elif choice == 3:
            pentagon(t1)
        elif choice == 4:
            star(t1)

        t1.end_fill()

# challenge
def complement():
    r = int(input("Enter red number: "))
    g = int(input("Enter green number: "))
    b = int(input("Enter blue number: "))
    turtle.colormode(255)
    turtle.bgcolor(255 - r, 255 - g, 255 - b)
    turtle.setup(width = 300, height = 300)
