
def orange(x):
	if x == 0:
		return 0

	ans = 0
	for i in range(1, x + 1):
		ans += i

	print(ans)
	return orange(x - 1) + ans
	
print(orange(23))


def sa(x):
	if x == 1: return 1

	return x + sa(x - 1)

print((sa(22) * 4) + (22 + 22 + 22) * 3 + 1)


def square(x):
	sum = 0
	for i in range(1, 23):
		sum += i ** 2
	return sum

print(square(23))