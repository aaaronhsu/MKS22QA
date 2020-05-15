from matplotlib import pyplot as plot
from matplotlib import style
# classwork/homework
def line():
    x = [5, 8, 10]
    y = [12, 16, 6]
    plot.plot(x, y)
    plot.title("Info")
    plot.xlabel("X axis")
    plot.ylabel("Y axis")
    plot.show()

def color():
    style.use("ggplot")
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
    plot.show()

def bar():
    plot.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label = 'Example one', color = 'b')
    plot.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label = 'Example two', color = 'g')

    plot.title("Info")
    plot.xlabel("X axis")
    plot.ylabel("Y axis")
    plot.legend()
    plot.show()

def scatter():
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [5, 2, 4, 2, 1, 4, 5, 2]

    plot.scatter(x, y, label = 'skitscat', color = 'k')
    plot.title("Info")
    plot.xlabel("X axis")
    plot.ylabel("Y axis")
    plot.legend()
    plot.show()

def stack():
    days = [1, 2, 3, 4, 5]
    sleeping = [7, 8, 6, 11, 7]
    eating = [2, 3, 4, 3, 2]
    working = [7, 8, 7, 2, 2]
    playing = [8, 5, 7, 8, 13]

    plot.plot([], [], color = 'm', label = 'Sleeping', linewidth = 5)
    plot.plot([], [], color = 'c', label = 'Eating', linewidth = 5)
    plot.plot([], [], color = 'r', label = 'Working', linewidth = 5)
    plot.plot([], [], color = 'k', label = 'Playing', linewidth = 5)

    plot.stackplot(days, sleeping, eating, working, playing, colors = ['m', 'c', 'r', 'k'])
    
    plot.title("Info")
    plot.xlabel("X axis")
    plot.ylabel("Y axis")
    plot.legend()
    plot.show()