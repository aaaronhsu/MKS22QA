import requests

response = requests.get('https://api.open5e.com/spells/')
data = response.json()
spells = data['results']

for i in spells:
	print(i['name'])


	