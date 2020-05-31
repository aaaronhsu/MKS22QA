#!/usr/bin/python
print("Content-type: text/html\n")

import cgi, cgitb

outline = '''<html> <head> <title> Login </title> </head>
<body>
	$$$output$$$
</body>
</html>'''

HTML = outline

form = cgi.FieldStorage()

username = form.getvalue('username', '')
password = form.getvalue('password', '')
name = form.getvalue('name', '')

HTML = HTML.replace('???username???', username)
HTML = HTML.replace('???password???', password)
HTML = HTML.replace('???name???', name)

login = False

# data parser
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

output = ''

if login:
	output = "you are logged in as $$$username$$$"
else:
	output = "bad"

print(HTML)