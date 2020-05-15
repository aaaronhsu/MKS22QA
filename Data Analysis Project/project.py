import pandas as pd
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
data = {'Items':['Toilet Paper(Small Pack, 12)', 'Toilet Paper(Bulk, 24)',
         'Hand Sanitizer(travel size, 2 fl. oz.)', 'Hand Sanitizer (medium size, 12 fl. oz.)',
         'Poland Spring Water Jug (1 Gallon)', 'Poland Spring Pack (24 Bottles)',
         'Heavy Duty Wipes (60 ct)', 'Heavy Duty Wipes (30 ct)'],
        'Price Before Corona': [11.98, 5.99, 1.79, 9.99, 17.88,
                                20.19, 7.98, 4.83],
        'Price After Corona': [12.48, 9.99, 1.79, 8.45, 20.36,
                               15.72, 8.71, 5.23],
        'Inflation %': [14.17, 66.78, 0.00, -15.42, 13.87,
                        22.14, 9.15, 8.28]}
df = pd.DataFrame(data, columns = ['Items', 'Price Before Corona',
                                          'Price After Corona', 'Inflation %'])
root= Tk() 
figure1 = plt.Figure(figsize=(8, 10), dpi=100)
ax1 = figure1.add_subplot(211)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=RIGHT, fill=BOTH)
df = df[['Items', 'Price Before Corona', 'Price After Corona', 'Inflation %']].groupby('Items').sum()
df.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Prices of Items Before and After Coronavirus')
root2 = Tk()
def update():
    data = {'Items':['Toilet Paper(Small Pack, 12)', 'Toilet Paper(Bulk, 24)',
         'Hand Sanitizer(travel size, 2 fl. oz.)', 'Hand Sanitizer (medium size, 12 fl. oz.)',
         'Poland Spring Water Jug (1 Gallon)', 'Poland Spring Pack (24 Bottles)',
         'Heavy Duty Wipes (60 ct)', 'Heavy Duty Wipes (30 ct)'],
        'Price Before Corona': [20, 5.99, 1.79, 9.99, 17.88,
                                20.19, 7.98, 4.83],
        'Price After Corona': [30, 9.99, 1.79, 8.45, 20.36,
                               15.72, 8.71, 5.23],
        'Inflation %': [50, 66.78, 0.00, -15.42, 13.87,
                        22.14, 9.15, 8.28]}
    df = pd.DataFrame(data, columns = ['Items', 'Price Before Corona',
                                          'Price After Corona', 'Inflation %'])
    figure1 = plt.Figure(figsize=(8, 10), dpi=100)
    ax1 = figure1.add_subplot(211)
    bar1 = FigureCanvasTkAgg(figure1, root2)
    bar1.get_tk_widget().pack(side=RIGHT, fill=BOTH)
    df = df[['Items', 'Price Before Corona', 'Price After Corona', 'Inflation %']].groupby('Items').sum()
    df.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Prices of Items Before and After Coronavirus')
btn = Button(root, text='Update?', command=update)
btn.pack()
mainloop()