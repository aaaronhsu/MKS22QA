def function(x):
	if x == 0:
		return

	print(x)
	function(x - 1)

function(5)
