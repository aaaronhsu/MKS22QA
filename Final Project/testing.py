username = "bob"
password = "gay"
login = False
accounts = {}
with open('accounts.csv') as f:
	data = f.readlines()
	for i in range(len(data) - 1):
		data[i] = data[i][:-1]
		data[i] = data[i].split(',')

	data[len(data) - 1] = data[len(data) - 1].split(',')

	accounts[data[0][0]] = []
	accounts[data[0][1]] = []
	accounts[data[0][2]] = []

	for i in range(1, len(data)):
		accounts['username'].append(data[i][0])
		accounts['password'].append(data[i][1])
		accounts['name'].append(data[i][2])

if username in accounts['username']:
	if password == accounts['password'][accounts['username'].index(username)]:
		login = True

print(login)