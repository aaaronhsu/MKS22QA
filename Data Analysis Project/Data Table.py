# Also download prices.csv and change the path of the file on line 15
# make sure that you have pip3 install pandas

import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def graph():
    
    print(toiletPaperL.get())

    data = {'Items': [],
            'Price Before Corona': [],
            'Price After Corona': [],
            'Inflation %': []}

    # reading file and parsing data
    with open('D://Coding/Python/AnnualPython/Data Analysis Project/prices.csv', 'r') as f:
        read = f.readlines()
    
    for i in range(len(read)):
        read[i] = read[i].split(', ')
        read[i][1] = float(read[i][1])
        read[i][2] = float(read[i][2])
        read[i][3] = float(read[i][3])
    
    
    # determines which items to graph
    requested = []
    if toiletPaperS.get(): requested.append(0)
    if toiletPaperL.get(): requested.append(1)
    if handSanitizerS.get(): requested.append(2)
    if handSanitizerL.get(): requested.append(3)
    if waterGal.get(): requested.append(4)
    if waterBot.get(): requested.append(5)
    if wipesS.get(): requested.append(6)
    if wipesL.get(): requested.append(7)

    # adds requested data to the data variable
    for i in requested:
        data['Items'].append(read[i][0])
        data['Price Before Corona'].append(read[i][1])
        data['Price After Corona'].append(read[i][2])
        data['Inflation %'].append(read[i][3])

    # creation of graph
    df = pd.DataFrame(data, columns = ['Items', 'Price Before Corona',
                                          'Price After Corona', 'Inflation %'])
    figure1 = plt.Figure(figsize=(6, 6), dpi=100)
    ax1 = figure1.add_subplot(211)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack()
    df = df[['Items', 'Price Before Corona', 'Price After Corona', 'Inflation %']].groupby('Items').sum()
    df.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Prices of Items Before and After Coronavirus')


root= Tk()

# values of checkbox variables
toiletPaperS = BooleanVar()
toiletPaperL = BooleanVar()
handSanitizerS = BooleanVar()
handSanitizerL = BooleanVar()
waterGal = BooleanVar()
waterBot = BooleanVar()
wipesS = BooleanVar()
wipesL = BooleanVar()

# checkboxes
Checkbutton(root, text = 'Toilet Paper (Small Pack, 12)', variable = toiletPaperS, onvalue = 1, offvalue = 0).pack()
Checkbutton(root, text = 'Toilet Paper (Bulk, 24)', variable = toiletPaperL, onvalue = 1, offvalue = 0).pack()
Checkbutton(root, text = 'Hand Sanitizer (travel size, 2 fl. oz.)', variable = handSanitizerS, onvalue = 1, offvalue = 0).pack()
Checkbutton(root, text = 'Hand Sanitizer (medium size, 12 fl. oz.)', variable = handSanitizerL, onvalue = 1, offvalue = 0).pack()
Checkbutton(root, text = 'Poland Spring Water Jug (1 Gallon)', variable = waterGal, onvalue = 1, offvalue = 0).pack()
Checkbutton(root, text = 'Poland Spring Pack (24 Bottles)', variable = waterBot, onvalue = 1, offvalue = 0).pack()
Checkbutton(root, text = 'Heavy Duty Wipes (30 ct)', variable = wipesS, onvalue = 1, offvalue = 0).pack()
Checkbutton(root, text = 'Heavy Duty Wipes (60 ct)', variable = wipesL, onvalue = 1, offvalue = 0).pack()

# button that creates graph
updateButton = Button(root, text = 'Graph', command = graph)
updateButton.pack()



root.mainloop()