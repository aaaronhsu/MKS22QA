

def total_pop(line):
	pop = line.split(',')
	total = 0
	for i in pop:
		total += int(i)
	
	return line + ',' + str(total)

print(total_pop('1,2,3,4'))