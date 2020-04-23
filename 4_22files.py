# classwork/homework
def readAll(fileName):
    f = open('test.txt', 'r')
    t = f.read()
    f.close()
    return t

def readFirst(fileName, n):
    f = open('test.txt', 'r')
    l = []
    for i in range(n):
        l.append(f.readline()[:-1])
    f.close()
    return l

def readLast(fileName, n):
    f = open('test.txt', 'r')
    l = f.readlines()
    f.close()
    for i in range(len(l) - n, len(l) - 1):
        l[i] = l[i][:-1]
    return l[-n:]

def readLines(fileName):
    f = open('test.txt', 'r')
    l = f.readlines()
    for i in range(len(l) - 1):
        l[i] = l[i][:-1]
    f.close()
    return l

def countLines(fileName):
    f = open('test.txt', 'r')
    l = f.readlines()
    f.close()
    return len(l)


def test(fileName):
    f = open('test.txt', 'r')
    count = 0
    for i in f:
        if '\n' in i:
            count += 1

    return count

print(test('text.txt'))