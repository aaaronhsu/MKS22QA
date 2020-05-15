from tkinter import BooleanVar, Button, Canvas, Checkbutton, IntVar, Label, PhotoImage, Tk, mainloop, simpledialog
import matplotlib.pyplot as plt
import requests
from random import uniform
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import re

path = 'D://Coding/Python/AnnualPython/Data Analysis Project/' # path of root folder ex: 'D://Python/Data Analysis Project/'

# Menu
def menuWindow(previousWindow = None):
        # opens menu and hides previous window
        menu = Tk()
        menu.geometry('600x200')
        menu.configure(bg='light cyan')
        menu.title('Menu')

        # title
        label = Label(menu, text = 'Effects of COVID-19\nBy Aaron Hsu, Ella Krechmer,\nSasha Motiellal, Maret Aulenbach,\nLogan Byers, and Israel Pina',
              bd = 1,
              relief = 'solid',
              font = 'Times 12',
              width = 30,
              height = 4,
              bg='white')
        label.pack()
        if previousWindow is not None:
                previousWindow.withdraw()


        # creates buttons for each section
        pricesButton = Button(menu, text = 'Changes in Cost of Items', command = lambda:pricesWindow(menu), bg = 'white')
        pollutionButton = Button(menu, text = 'Changes in Pollution Levels', command = lambda:pollutionWindow(menu), bg='white')
        deathsButton = Button(menu, text = 'Death Count', command = lambda:deathWindow(menu), bg='white')
        pricesButton.place(x=70, y=125)
        pollutionButton.place(x=370, y=125)
        deathsButton.place(x=250, y = 125)



# Prices
def pricesWindow(previousWindow):
        # closes menu and opens prices window
        pricesSelection = Tk()
        previousWindow.withdraw()
        pricesSelection.configure(bg='light cyan')
        pricesSelection.title('Prices of Items')
        pricesSelection.geometry('400x310')
        label = Label(pricesSelection, text = 'Select item(s):',
              bd = 0,
              relief = 'solid',
              width = 15,
              height = 2,
              bg = 'light cyan')
        label.pack()
        
        # values of checkbox variables
        toiletPaperS = BooleanVar(pricesSelection)
        toiletPaperL = BooleanVar(pricesSelection)
        handSanitizerS = BooleanVar(pricesSelection)
        handSanitizerL = BooleanVar(pricesSelection)
        waterGal = BooleanVar(pricesSelection)
        waterBot = BooleanVar(pricesSelection)
        wipesS = BooleanVar(pricesSelection)
        wipesL = BooleanVar(pricesSelection)

        # creation of checkboxes
        Checkbutton(pricesSelection, text = 'Toilet Paper (Small Pack, 12)', variable = toiletPaperS, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(pricesSelection, text = 'Toilet Paper (Bulk, 24)', variable = toiletPaperL, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(pricesSelection, text = 'Hand Sanitizer (travel size, 2 fl. oz.)', variable = handSanitizerS, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(pricesSelection, text = 'Hand Sanitizer (medium size, 12 fl. oz.)', variable = handSanitizerL, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(pricesSelection, text = 'Poland Spring Water Jug (1 Gallon)', variable = waterGal, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(pricesSelection, text = 'Poland Spring Pack (24 Bottles)', variable = waterBot, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(pricesSelection, text = 'Heavy Duty Wipes (30 ct)', variable = wipesS, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(pricesSelection, text = 'Heavy Duty Wipes (60 ct)', variable = wipesL, onvalue = 1, offvalue = 0, bg='light cyan').pack()

        # button that creates graph
        graphPrices = Button(pricesSelection, text = 'Graph Selected', bg='white', command = lambda:pricesData([toiletPaperS, toiletPaperL, handSanitizerS, handSanitizerL, waterGal, waterBot, wipesS, wipesL]))
        graphPrices.place(x=50, y=250)
       
        # button that graphs all
        graphAll = Button(pricesSelection, text = 'Graph All', bg='white', command = lambda:pricesData())
        graphAll.place(x=168, y=250)
       
        # return to menu button
        menuButton = Button(pricesSelection, text = 'Return to Menu', bg='white', command = lambda:menuWindow(pricesSelection))
        menuButton.place(x=250, y=250)
        
def pricesData(checkboxes = None):
        data = {'Items': [],
        'Price Before Corona': [],
        'Price After Corona': [],
        'Inflation %': []}

        # reading file and parsing data
        with open(path + 'prices.csv', 'r') as f:
                read = f.readlines()
    
        for i in range(len(read)):
                read[i] = read[i].split(',')
                read[i][1] = float(read[i][1])
                read[i][2] = float(read[i][2])
                read[i][3] = float(read[i][3])
    
    
        requested = []
        if checkboxes is not None:
        # determines which items to graph
                for i in range(len(checkboxes)):
                        if checkboxes[i].get(): requested.append(i)
        else:
                for i in range(8):
                        requested.append(i)

        # adds requested data to the data variable
        for i in requested:
                data['Items'].append(read[i][0])
                data['Price Before Corona'].append(read[i][1])
                data['Price After Corona'].append(read[i][2])
                data['Inflation %'].append(read[i][3])

        # graphing function
        graphPrices(data)

def graphPrices(data):
        # create window for price graph
        priceGraph = Tk()

        # creation of figure for graph
        df = pd.DataFrame(data, columns = ['Items', 'Price Before Corona',
                                          'Price After Corona', 'Inflation %'])
        figure1 = plt.Figure(figsize=(6, 6), dpi=100)
        ax1 = figure1.add_subplot(211)
        bar1 = FigureCanvasTkAgg(figure1, priceGraph)
        bar1.get_tk_widget().pack()
        df = df[['Items', 'Price Before Corona', 'Price After Corona', 'Inflation %']].groupby('Items').sum()
        df.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Prices of Items Before and After Coronavirus')



# Pollution
def pollutionWindow(previousWindow):
        # closes menu and opens pollution window
        countrySelection = Tk()
        previousWindow.withdraw()
        countrySelection.geometry('400x225')
        countrySelection.configure(bg='light cyan')

        # values of checkboxes
        europe = BooleanVar(countrySelection)
        china = BooleanVar(countrySelection)
        unitedStates = BooleanVar(countrySelection)
        india = BooleanVar(countrySelection)
        glob = BooleanVar(countrySelection)

        # creation of checkboxes
        Checkbutton(countrySelection, text = 'Europe', variable = europe, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(countrySelection, text = 'China', variable = china, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(countrySelection, text = 'United States', variable = unitedStates, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(countrySelection, text = 'India', variable = india, onvalue = 1, offvalue = 0, bg='light cyan').pack()
        Checkbutton(countrySelection, text = 'Global', variable = glob, onvalue = 1, offvalue = 0, bg='light cyan').pack()

        # button that creates graph
        graphPrices = Button(countrySelection, text = 'Graph', command = lambda:pollutionData([europe, china, unitedStates, india, glob]), bg='white')
        graphPrices.place(x=97, y=150)
       
        # button that graphs all
        graphAll = Button(countrySelection, text = 'Graph All', command = lambda:pollutionData(), bg = 'white')
        graphAll.place(x=150, y=150)
        
        # return to menu button
        menuButton = Button(countrySelection, text = 'Return to Menu', command = lambda:menuWindow(countrySelection), bg='white')
        menuButton.place(x=220, y=150)
       
def pollutionData(checkboxes = None):
        with open(path + 'pollution.csv', 'r') as f:
                read = f.readlines()
        
        data = {'Countries': [], 
                        'Pollution estimate before': [], 
                        'Pollution estimate after': []}

        for i in range(len(read)):
                read[i] = read[i].split(',')
                read[i][1] = float(read[i][1])
                read[i][2] = float(read[i][2][:-2])

        if checkboxes is not None:
                # if user decides to only graph certain countries
                requested = []
                for i in range(len(checkboxes)):
                        if bool(checkboxes[i].get()): requested.append(i)
                
                for i in requested:
                        data['Countries'].append(read[i][0])
                        data['Pollution estimate before'].append(read[i][1])
                        data['Pollution estimate after'].append(read[i][2])
        else:
                # user wants all data
                for i in range(len(read)):
                        data['Countries'].append(read[i][0])
                        data['Pollution estimate before'].append(read[i][1])
                        data['Pollution estimate after'].append(read[i][2])

        graphPollution(data)

def graphPollution(data):
        # create window for pollution graph
        pollutionGraph = Tk()

        # creation of dataframe to house graph
        df = pd.DataFrame(data, columns = ['Countries', 'Pollution estimate before',
                                          'Pollution estimate after'])
        figure1 = plt.Figure(figsize=(6, 6), dpi=100)
        ax1 = figure1.add_subplot(211)
        bar1 = FigureCanvasTkAgg(figure1, pollutionGraph)
        bar1.get_tk_widget().pack()
        df = df[['Countries', 'Pollution estimate before', 'Pollution estimate after']].groupby('Countries').sum()
        df.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Estimates of Change In Pollution for 2020 (by % change)')



# Deaths
def deathWindow(previousWindow):
        # closes menu and prompts user for a country
        previousWindow.withdraw()

        # asks user to input country
        unformattedCountry = simpledialog.askstring('Country', 'Insert Country (ex: South Africa):')
        if unformattedCountry is None:
                menuWindow()

        # formats the userinput to work with API
        formattedCountry = ''
        for i in unformattedCountry.split(' '):
                formattedCountry += i.lower()
                formattedCountry += '-'
        formattedCountry = formattedCountry[:-1]


        # asks user to input start date
        unformattedStartDate = simpledialog.askstring('Start Date', 'Insert Start Date (ex: 4/14):')
        if unformattedStartDate is None:
                menuWindow()
        
        formattedStartDate = ''
        for i in unformattedStartDate.split('/'):
                if int(i) < 10:
                        formattedStartDate += '0' + i + '-'
                else:
                        formattedStartDate += i + '-'
        formattedStartDate = formattedStartDate[:-1]

        # asks user to input end date
        unformattedEndDate = simpledialog.askstring('End Date', 'Insert End Date (ex: 4/28):')
        if unformattedEndDate is None:
                menuWindow()

        formattedEndDate = ''
        for i in unformattedEndDate.split('/'):
                if int(i) < 10:
                        formattedEndDate += '0' + i + '-'
                else:
                        formattedEndDate += i + '-'
        formattedEndDate = formattedEndDate[:-1]
        

        deathData(formattedCountry, formattedStartDate, formattedEndDate)


def deathData(country, start, end):
        # pulls info from API
        url = 'https://api.covid19api.com/total/country/' + country

        payload = {}
        headers= {}

        response = requests.request("GET", url, headers=headers, data = payload)

        unformattedData = str(response.text.encode('utf8'))
        
        # finds the index of each occurance of keyword and puts in a list
        confirmed = [m.start() for m in re.finditer("\"Confirmed\": ", unformattedData)]
        deaths = [m.start() for m in re.finditer("\"Deaths\": ", unformattedData)]
        recovered = [m.start() for m in re.finditer("\"Recovered\": ", unformattedData)]
        active = [m.start() for m in re.finditer("\"Active\": ", unformattedData)]
        date = [m.start() for m in re.finditer("\"Date\": ", unformattedData)]

        data = {'Date': [], 
                'Confirmed': [],
                'Deaths': [],
                'Recovered': [],
                'Active': [],}

        # isolates the data by shifting indexes of keywords
        for i in range(len(confirmed)):
                data['Confirmed'].append(int(unformattedData[confirmed[i] + 13 : deaths[i] - 7]))
                data['Deaths'].append(int(unformattedData[deaths[i] + 10 : recovered[i] - 7]))
                data['Recovered'].append(int(unformattedData[recovered[i] + 13 : active[i] - 7]))
                data['Active'].append(int(unformattedData[active[i] + 10 : date[i] - 7]))
                data['Date'].append(unformattedData[date[i] + 14 : date[i] + 19])

        # updates data so that it only contains data within timeframe                
        startIndex = data['Date'].index(start)
        endIndex = data['Date'].index(end) + 1

        data['Confirmed'] = data['Confirmed'][startIndex : endIndex]
        data['Deaths'] = data['Deaths'][startIndex : endIndex]
        data['Recovered'] = data['Recovered'][startIndex : endIndex]
        data['Active'] = data['Active'][startIndex : endIndex]
        data['Date'] = data['Date'][startIndex : endIndex]

        graphDeaths(data, country)

def graphDeaths(data, country):
        # graphs data for confirmed, deaths, active, and recovery

        plt.plot (data['Date'], data['Confirmed'],
                  label = 'Confirmed')
        plt.plot (data['Date'], data['Deaths'],
                  label = 'Deaths')
        plt.plot (data['Date'], data['Recovered'],
                  label = 'Recovered')
        plt.plot (data['Date'], data['Active'],
                  label = 'Active')

        plt.title(country[0].upper() + country[1:])
        plt.ylabel('People')
        plt.xlabel('Date')

        plt.legend(frameon = False)
        plt.grid(True, color = 'k')
        
        if len(data['Date']) > 30: 
                # hides x-axis if there are than 30 days
                plt.xticks(color='w')
        menuWindow()
        plt.show()

# starts program
menuWindow()
mainloop()

