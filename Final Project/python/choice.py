#!/usr/bin/python
print("Content-type: text/html\n")

import cgi, cgitb

def htmlTop():
	print ('''\n\n
	<!DOCTYPE html>
	<html lang="en-US">
		<head> 
		 <link rel="icon" type="image/png" href="../images/chickenNugget.png">
		 <title>Chicken Nugget Crisis</title> 
		 <meta charset="UTF-8">
		 <link rel="stylesheet" type="text/css" href="../css/global.css">
		 <link rel="stylesheet" type="text/css" href="../css/choice.css">
		 <style>
			 
		 </style>
	 </head> 
		<body>
			<div class="nav">
				<a href="../sources.html">Sources</a>
				<a href="../news.html">News</a>
				<a href="../index.html">Home</a>
				 
				<a class="active" href="../save.html">Save the World</a>
	
				<p class="header">The Chicken Nugget</p>
			</div>''')

def htmlTail():
	print('''
		</body>
	</html>''')


def getData():
	form = cgi.FieldStorage()
	name = form.getvalue("name")
	money = form.getvalue("money")
	day = form.getvalue("day")

	if name != None:
		s = '''<h1> Day ''' + day + ''' of ''' + name + ''': What will the choice be today?'''
		
		form = '''<form method="post" action="result.py">
		<label for="baseSelect">Choose a base:</label>
		<select name="Base" id="baseSelect">
			<option>Soybean</option>
			<option>Duck</option>
			<option>Flamingo</option>
			<option>Cardboard</option>
		</select>
	
		<label for="breadingSelect">Choose a breading:</label>
		<select name="Breading" id="breadingSelect">
			<option>Breadcrumbs</option>
			<option>Panko Crumbs</option>
			<option>Crushed Peanuts</option>
			<option>No Breading</option>
		</select>
	
		<label for="cookSelect">Choose a cooking method:</label>
		<select name="Method of Cooking" id="cookSelect">
			<option>Deep-fry</option>
			<option>Air-fry</option>
			<option>Boil</option>
			<option>Don’t</option>
		</select>
	
		<label for="dipSelect">Choose a dipping sauce:</label>
		<select name="Dipping Sauce" id="dipSelect">
			<option>Ketchup</option>
			<option>BBQ Sauce</option>
			<option>Soy Sauce</option>
			<option>No Sauce</option>
		</select>

		<input type="hidden" id="day" name="day" value="''' + day + '''">
		<input type="hidden" id="money" name="money" value="''' + money + '''">
		<input type="hidden" id="name" name="name" value="''' + name + '''">

		<br>
		<input class="larger" type="submit" value="Make the nugget!">
	</form>'''


		ingredients = '''
			<h2>Buy your ingredients! You have <span class="green">$''' + money + '''</span> in your bank account</h2>
			<div class="center">
				<table class="center">
					<tr>
						<th>Category</th>
						<th>Information</th>
					</tr>

					<tr>
						<td>Base</td>
						<center>
						<td class="innerCenter">
						<table>
							<tr>
								<th>Option</th>
								<th>Price</th>
							</tr>
							<tr>
								<td>Soybean</td>
								<td>$5</td>
							</tr>
							<tr>
								<td>Duck</td>
								<td>$6</td>
							</tr>
							<tr>
								<td>Flamingo</td>
								<td>$10</td>
							</tr>
							<tr>
								<td>Cardboard</td>
								<td>$1</td>
							</tr>
						</table>
						</td>
						</center>
					</tr>

					<tr>
						<td>Breading</td>
						<td class="innerCenter">
						<table>
							<tr>
								<th>Option</th>
								<th>Price</th>
							</tr>
							<tr>
								<td>Breadcrumbs</td>
								<td>$3</td>
							</tr>
							<tr>
								<td>Panko Crumbs</td>
								<td>$3</td>
							</tr>
							<tr>
								<td>Crushed Peanuts</td>
								<td>$4</td>
							</tr>
							<tr>
								<td>No Breading</td>
								<td>FREE</td>
							</tr>
						</table>
						</td>
					</tr>

					<tr>
						<td>Cooking Method</td>
						<td class="innerCenter">
						<table>
							<tr>
								<th>Option</th>
								<th>Price</th>
							</tr>
							<tr>
								<td>Deep-fry</td>
								<td>$2</td>
							</tr>
							<tr>
								<td>Air Fry</td>
								<td>$1</td>
							</tr>
							<tr>
								<td>Boil</td>
								<td>$1</td>
							</tr>
							<tr>
								<td>Don't Cook</td>
								<td>FREE</td>
							</tr>
						</table>
						</td>
					</tr>

					<tr>
						<td>Dipping Sauce</td>
						<td class="innerCenter">
						<table>
							<tr>
								<th>Option</th>
								<th>Price</th>
							</tr>
							<tr>
								<td>Ketchup</td>
								<td>$1</td>
							</tr>
							<tr>
								<td>BBQ Saunce</td>
								<td>$1</td>
							</tr>
							<tr>
								<td>Soy Sauce</td>
								<td>$1</td>
							</tr>
							<tr>
								<td>No Dipping Sauce</td>
								<td>FREE</td>
							</tr>
						</table>
						</td>
					</tr>
				</table>
			</div>
		'''
		print(s)
		print(form)
		print(ingredients)
	else:
		print('''<h1>You can't name a restaurant nothing! Click <a href="../save.html">here</a> to go back.</h1>''')
def main():
	htmlTop()
	getData()
	htmlTail()

if __name__ == '__main__':
	try:
		main()
	except:
		cgi.print_exception()