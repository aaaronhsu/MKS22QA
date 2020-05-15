from turtle import *
# classwork
def koch(t, o, s):
    if o == 0:
        t.fd(s)
    else:
        koch(t, o - 1, s / 3)
        t.lt(60)
        koch(t, o - 1, s / 3)
        t.rt(120)
        koch(t, o - 1, s / 3)
        t.lt(60)
        koch(t, o - 1, s / 3)

def triangle(t, o, s):
    for i in range(3):
        t.rt(120)
        koch(t, o, s)


triangle(Turtle(), 3, 100)
