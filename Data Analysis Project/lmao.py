import requests
import re

country = input('Input country')
url = 'https://api.covid19api.com/total/country/' + country

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

unformattedData = str(response.text.encode('utf8'))

confirmed = [m.start() for m in re.finditer("\"Confirmed\": ", unformattedData)]
deaths = [m.start() for m in re.finditer("\"Deaths\": ", unformattedData)]
recovered = [m.start() for m in re.finditer("\"Recovered\": ", unformattedData)]
active = [m.start() for m in re.finditer("\"Active\": ", unformattedData)]
date = [m.start() for m in re.finditer("\"Date\": ", unformattedData)]


f = open('D://Coding/Python/AnnualPython/Data Analysis Project/test.txt', 'w')

# for i in range(len(start)):
# 	print(unformattedData[start[i] + 9 : end[i] - 7])
# 	f.write(unformattedData[start[i] + 9 : end[i] - 7] + '\n')
data = {'Date': [], 
		'Confirmed': [],
		'Deaths': [],
		'Recovered': [],
		'Active': [],}

for i in range(len(confirmed)):
	data['Confirmed'].append(unformattedData[confirmed[i] + 13 : deaths[i] - 7])
	data['Deaths'].append(unformattedData[deaths[i] + 10 : recovered[i] - 7])
	data['Recovered'].append(unformattedData[recovered[i] + 13 : active[i] - 7])
	data['Active'].append(unformattedData[active[i] + 10 : date[i] - 7])
	data['Date'].append(unformattedData[date[i] + 14 : date[i] + 19])

print(data['Date'])


f.write(unformattedData)

f.close()