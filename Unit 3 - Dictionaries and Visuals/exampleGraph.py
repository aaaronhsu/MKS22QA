from tkinter import *
import numpy as np
import matplotlib.pyplot as plot

root = Tk()
root.title('Test')
root.iconbitmap('D://Coding/Python/AnnualPython/test.txt')
root.geometry('400x200')

potato = False
def graph():
        house_prices = np.random.normal(200000, 25000, 5000)
        plot.hist(house_prices, 50)
        plot.show()

def color():
    x = [5, 8, 10]
    y = [12, 16, 6]

    x2 = [6, 9, 11]
    y2 = [6, 15, 7]

    plot.plot(x, y, label = 'lineOne', linewidth = 5)
    plot.plot(x2, y2, label = 'lineTwo', linewidth = 5)

    plot.title("Info")
    plot.xlabel("X axis")
    plot.ylabel("Y axis")
    plot.legend()
    plot.grid(True, color = 'k')
    # my_button.pack_forget()
    plot.show()

my_button = Button(root, text = 'Graph', command = graph)
my_button.pack()
other_button = Button(root, text = "asdfasdf", command = color)
other_button.pack()


root.mainloop()