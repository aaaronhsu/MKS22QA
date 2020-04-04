from turtle import *
from random import randint
# classwork/homework
def tree(bL, t):
    if bL > 5:
        t.pensize(bL ** 1.3 / 100)
        if bL < 15:
            t.pencolor("green")
        else:
            t.pencolor("brown")
        turn = randint(10, 30)
        decrease = randint(10, 20)

        t.fd(bL)
        t.rt(turn)
        tree(bL - decrease, t)
        t.lt(turn * 2)
        tree(bL - decrease, t)
        t.rt(turn)
        t.bk(bL)

def main():
    t = Turtle()
    tree(100, t)
