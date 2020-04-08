from tkinter import *
import time
from random import randint

tk = Tk()

canvas = Canvas(tk, width=400, height=400)

canvas.pack()

canvas.create_polygon(10, 10, 10, 20, 20, 20, 20, 10, fill = "red")
tk.update()

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
        
    tk.update()

def teleport(event):
    canvas.move(1, randint(0, 20), randint(0, 20))
    tk.update()


canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
canvas.bind_all('<KeyPress-Return>', teleport)

mainloop()