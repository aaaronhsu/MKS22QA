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
		 <link rel="stylesheet" type="text/css" href="../css/save.css">
		 <link rel="stylesheet" type="text/css" href="../css/login.css">
		 <link rel="stylesheet" type="text/css" href="../css/result.css">
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
			</div>
			
			<div class="information">''')

def htmlTail():
	print('''
		</body>
	</html>''')


def getData():
	form = cgi.FieldStorage()
	base = form.getvalue("Base")
	breading = form.getvalue("Breading")
	cook = form.getvalue("Method of Cooking")
	dip = form.getvalue("Dipping Sauce")

	money = form.getvalue("money")
	day = form.getvalue("day")
	name = form.getvalue("name")

	nextDay = int(day) + 1
	nextMoney = int(money)

	baseC = ""
	breadingC = ""
	cookC = ""
	dipC = ""
	points = 0
	cost = 0

	soybean = {"price": 5, "pts": 3, "desc":"A sustainable choice, people admire your efforts to make your food appealing for vegetarians, but the texture just isn’t the same as chicken."}
	duck = {"price": 6, "pts": 3, "desc":"Textbook alternative. You serve your duck nuggets to your customers and the meat tastes fine. Nothing special, but nothing “chicken” worthy."}
	flamingo = {"price": 10, "pts": 5, "desc":"An exotic choice! Customers from around the nation flock to your restaurant to try your flamingo nugget. The meat resembles the taste of chicken, but with a hint of seafood."}
	cardboard = {"price": 1, "pts": 0, "desc":"While cheap, you notice that cardboard is unfortunately inedible. But you don’t care. You serve your cardboard nuggets to your customers, and they choke to death because they can’t swallow your nuggets."}

	breadcrumbs = {"price": 3, "pts": 1, "desc":"Generic. Your customers are satisfied with the classic breadcrumbs."}
	panko = {"price": 3, "pts": 2, "desc":"A crunchy alternative to the classic breadcrumb. Your customers enjoy the extra texture."}
	peanuts = {"price": 4, "pts": 0, "desc":"Unfortunately, you forget to include that the peanuts are in the nuggets. A couple of your customers have allergic reactions, and one of them is sent to the hospital. You are now being pursued by multiple lawyers."}
	noBreading = {"price": 0, "pts": 0, "desc":"You choose to take the cheap option. You want to save some money so that you can spend it on your Fortnite account. However, your customers aren’t interested in your Fortnite account, and are left unsatisfied."}

	deepfry = {"price": 2, "pts": 2, "desc":"Classic option. Adds some color and crunch and your customers like it."}
	airfry = {"price": 1, "pts": 1, "desc":"A healthy choice that adds some color, but lacks some flavor."}
	boil = {"price": 1, "pts": 0, "desc":"You crucify your nugget in boiling water, removing all of its flavor."}
	noCook = {"price": 0, "pts": -1, "desc":"Your customers are confused as to why you are selling a cook-your-own nugget."}

	ketchup = {"price": 1, "pts": 1, "desc":"It’s a time-tested classic, and satisfies your customers."}
	bbq = {"price": 1, "pts": 1, "desc":"A slightly tangy sauce, bringing a new flavor profile to the nugget."}
	soySauce = {"price": 1, "pts": 0, "desc":"It’s just salty water. This isn’t an Asian fusion restaurant."}
	noSauce = {"price": 0, "pts": 0, "desc":"You choose to save a bit of money on the sauce so that you can fund your Fortnite account."}


	if base == "Soybean":
		points += soybean["pts"]
		cost += soybean["price"]
		baseC = soybean["desc"]
	elif base == "Duck":
		points += duck["pts"]
		cost += duck["price"]
		baseC = duck["desc"]
	elif base == "Flamingo":
		points += flamingo["pts"]
		cost += flamingo["price"]
		baseC = flamingo["desc"]
	else:
		points += cardboard["pts"]
		cost += cardboard["price"]
		baseC = cardboard["desc"]


	if breading == "Breadcrumbs":
		points += breadcrumbs["pts"]
		cost += breadcrumbs["price"]
		breadingC = breadcrumbs["desc"]
	elif breading == "Panko Crumbs":
		points += panko["pts"]
		cost += panko["price"]
		breadingC = panko["desc"]
	elif breading == "Crushed Peanuts":
		points += peanuts["pts"]
		cost += peanuts["price"]
		breadingC = peanuts["desc"]
	else:
		points += noBreading["pts"]
		cost += noBreading["price"]
		breadingC = noBreading["desc"]

	
	if cook == "Deep-fry":
		points += deepfry["pts"]
		cost += deepfry["price"]
		cookC = deepfry["desc"]
	elif cook == "Air-fry":
		points += airfry["pts"]
		cost += airfry["price"]
		cookC = airfry["desc"]
	elif cook == "Boil":
		points += boil["pts"]
		cost += boil["price"]
		cookC = boil["desc"]
	else:
		points += noCook["pts"]
		cost += noCook["price"]
		cookC = noCook["desc"]


	if dip == "Ketchup":
		points += ketchup["pts"]
		cost += ketchup["price"]
		dipC = ketchup["desc"]
	elif dip == "BBQ Sauce":
		points += bbq["pts"]
		cost += bbq["price"]
		dipC = bbq["desc"]
	elif dip == "Soy Sauce":
		points += soySauce["pts"]
		cost += soySauce["price"]
		dipC = soySauce["desc"]
	else:
		points += noSauce["pts"]
		cost += noSauce["price"]
		dipC = noSauce["desc"]

	if points >= 10:
		mainStory = "You made the most chicken-like nugget that the world has ever seen. Customers around the world flock to your restaurant. You successfully saved the world from the chicken nugget crisis and world-renowned chefs such as Gordan Ramsay recognize your name as one of the greatest chefs of the millenia."
		income = 20
	elif points >= 7:
		mainStory = "Your nuggets are good. You make some friendly relationships with some of your customers and some of them even buy seconds. Although you may not have solved the chicken nugget crisis, your nuggets somewhat satisfy the crave for nuggets. Maybe something more exotic would appeal to the public."
		income = 15
	elif points >= 4:
		mainStory = "Your nuggets aren’t exactly what your customers expected. They recognize your efforts to make an avant garde nugget, but aren’t interested in buying more. It just doesn’t serve as a proper substitute for chicken nuggets."
		income = 5	
	elif points >= 0:
		mainStory = "Your nuggets kinda suck. The few customers that do choose to buy your nugget don’t even eat them. They just use them as stones to throw at you. Your public image is ruined and the news ridicules your restaurant as one of the worst to open since the beginning of time."
		income = -3
	else:
		mainStory = "Your nuggets are known to be one of the most toxic substances to man-kind. People evacuate from your restaurant and the FDA recommends the public to stay at least 500ft away from it. You literally made the worst nugget possible. Congrats."
		income = -10

	nextMoney -= cost
	nextMoney += income

	fin = ""
	fin += '''<h1>Verdict: ''' + mainStory + '''</h1>'''

	fin += '''<h2>This is what your customers have to say about each choice</h2>'''

	fin += '''
		<div class="center">
		  <table class="results">
				<tr>
					<th class="bottomBorder">Category</th>
					<th class="bottomBorder">Option</th>
					<th class="bottomBorder">Result</th>
				</tr>

				<tr>
					<td>Base</td>
					<td>''' + base + '''</td>
					<td>''' + baseC + '''</td>
				</tr>
				<tr>
					<td>Breading</td>
					<td>''' + breading + '''</td>
					<td>''' + breadingC + '''</td>
				
				</tr>
				<tr>
					<td>Cooking Method</td>
					<td>''' + cook + '''</td>
					<td>''' + cookC + '''</td>
				</tr>

				<tr>
					<td>Dipping Sauce</td>
					<td>''' + dip + '''</td>
					<td>''' + dipC + '''</td>
				</tr>
		  </table>
		</div>
		  '''
	

	if income - cost > 0:
		fin += '''<h3>Food critics rated your nugget a <span class="highlight">''' + str(points) + '''/10</span> and you gained <span class="green">$''' + str(income - cost) + '''</span> for the day</h3>'''
	elif points == -1:
		fin += '''<h3>Food critics refused to even rate your trash that you call a nugget and you lost <span class="red">$''' + str(abs(income - cost)) + '''</span> for the day</h3>'''
	else:
		fin += '''<h3>Food critics rated your nugget a <span class="highlight">''' + str(points) + '''/10</span> and you lost <span class="red">$''' + str(abs(income - cost)) + '''</span> for the day</h3>'''


	if nextMoney <= 0: 
		fin += '''</div>
		<form class="box" action="../save.html" method="post">
			<h1>You have no more money to continue your business...</h1>
			<input type="submit" name="submit" value="Go Back">
		</form>
		'''
	else:
		fin += '''</div>
		<form class="box" action="choice.py" method="post">
				<h1>Craft another nugget!</h1>
				<input type="hidden" id="name" name="name" value="''' + name + '''">
				<input type="hidden" id="day" name="day" value="''' + str(nextDay) + '''">
				<input type="hidden" id="money" name="money" value="''' + str(nextMoney) + '''">
				<input type="submit" name="submit" value="Next Day">
			</form>
			'''
	return fin

def main():
	htmlTop()
	print('{}'.format(getData()))
	htmlTail()

if __name__ == '__main__':
	try:
		main()
	except:
		cgi.print_exception()