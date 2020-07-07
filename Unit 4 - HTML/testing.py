#!/usr/bin/python
print("Content-type: text/html\n")

import cgi

def htmlTop():
	print ('''\n\n
	<!DOCTYPE html>
	<html lang="en-US">
		<head>
			<meta charset="utf-8">
			<title> Server-side script </title>
		</head>
		<body>''')

def htmlTail():
	print('''</body>
	</html>''')

def getData():
	form = cgi.FieldStorage()
	email = form.getvalue("email")

	with open("emails.csv", "rw+") as f:
		f.write(email)
	

def main():
	htmlTop()
	getData()
	print("congrats you did a thing")
	htmlTail()


if __name__ == '__main__':
	try:
		main()
	except:
		cgi.print_exception()
