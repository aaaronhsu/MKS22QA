from turtle import *
from random import randint

# create lines
setup(width = 300, height = 300)
set = Turtle()
set.pu()
set.ht()
set.goto(-100, 120)
for i in range(11):
    set.pd()
    set.write(i, align = 'center')
    set.rt(90)
    set.fd(10)
    set.pd()
    set.fd(200)
    set.pu()
    set.bk(210)
    set.lt(90)
    set.fd(20)

# create turtles
turtles = []
cor = []
for i in range(10):
    turtles += [Turtle()]
    cor += [0]
    turtles[i].pu()
    turtles[i].goto(-110, 100 - i * 20)

# turtle race
while max(cor) < 215:
    t = randint(0, 9)
    move = randint(0, 20)
    turtles[t].fd(move)
    cor[t] += move
    # makes current lead flash red
    for i in turtles:
        i.color("black")
    turtles[cor.index(max(cor))].color("red")
else:
    # turtle win
    win = cor.index(max(cor))
    print("Turtle", win, "won")
    win = turtles[cor.index(max(cor))]
    set.clear()

# hide all losing turtles
for i in turtles:
    if win != i:
        i.ht()

# win sequence
win.goto(0, 100)
win.write("Turtle " + str(cor.index(max(cor))) + " wins!", align = "center")
win.pu()

win.goto(0, 0)
win.speed(0)
win.pd()
win.pensize(1)
colormode(255)
for a in range(15):
    win.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(5):
        win.forward(50)
        win.right(144)
    win.left(24)
