#!/usr/bin/python
print("Content-type: text/html\n")

import cgi, cgitb

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
	drink = form.getvalue("drink")
	return drink

	

def main():
	htmlTop()
	print('You have selected {}'.format(getData()))
	htmlTail()

if __name__ == '__main__':
	try:
		main()
	except:
		cgi.print_exception()