# classwork/homework
def squares(n):
    d = {}
    for i in range(1, n + 1):
        d[i] = i * i
    return d

def sort(d):
    l = []
    for k,v in d.items():
        l.append([k, v])
    l.sort(key = lambda x: x[1])
    l.reverse()
    return l