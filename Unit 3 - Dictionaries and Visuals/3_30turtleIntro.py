import turtle
import random

# classwork
def star():
    t = turtle.Turtle()
    size = int(input("Enter a pen size: "))
    color = input("Enter a color: ")
    background = input("Enter a background color: ")

    t.pd()
    t.pensize(size)
    t.pencolor(color)

    turtle.speed(0)
    turtle.bgcolor(background)
    turtle.setup(width = 300, height = 300)

    for i in range(5):
        turtle.forward(50)
        turtle.right(144)


# homework
def spiralStar(l):
    t = turtle.Turtle()

    turtle.speed(0)
    t.pd()
    t.pensize(5)
    turtle.bgcolor("black")
    turtle.setup(width = 300, height = 300)

    for a in range(60):
        t.pencolor(l[random.randint(0, len(l) - 1)])
        for i in range(5):
            turtle.forward(50)
            turtle.right(144)
        turtle.left(6)
