d = {'Mount Everest': 8848, 
    'K2': 8611,
    'Kangchenjunga': 8586,
    'Lhotse': 8516,
    'Makalu': 8485}

def part1():
    count = 1
    for i in d:
        print("Mountain " + str(count) + ' is ' + i)
        count += 1

    count = 1
    for i in d:
        print('Mountain ' + str(count) + ' is ' + str(d[i]) + ' meters tall')
        count += 1

    for i,k in d.items():
        print(i + ' is ' + str(k) + ' meters tall.')

def part2():
    l = []
    for i,k in d.items():
        l.append([i, k])
    l.sort()
    for i in l:
        print(i[0] + ' is ' + str(i[1]) + ' meters tall.')

def part3():
    d2 = {}
    for i,k in d.items():
        d2[i] = [k, int(k * 3.28)]
    
    for i in d2:
        print(i)

    for i in d2:
        print(d2[i][0])
    
    for i in d2:
        print(d2[i][1])

    for i,k in d2.items():
        print(i + ' is ' + str(k[0]) + ' meters tall, or ' + str(k[1]) + ' feet.')
    
part1()