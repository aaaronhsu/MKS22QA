import requests

url = 'https://api.covid19api.com/total/country/china'
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data = payload)
data = str(response.text.encode('utf8'))
print(data)


