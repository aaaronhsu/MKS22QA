from turtle import *
from tkinter import *
# classwork/homework
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

tk = Tk()
btn = Button(tk, text = "create snowflake", command = lambda:triangle(Turtle(), 3, 100))
btn.pack()
mainloop()
