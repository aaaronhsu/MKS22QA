# classwork/homework
def duplicate(d):
    # removes keys with duplicate values
    seen = []
    delete = []
    for k in d:
        if d[k] in seen: delete += [k]
        else: seen += [d[k]]
    
    for k in delete:
        d.pop(k)

    return d

def empty(d):
    return not bool(d)

def highest(d):
    l = list(d.values())
    l.sort()
    return l[-3:]

# challenge
def dict(l1, l2):
    d = {}
    for k in range(len(l1)):
        d[l1[k]] = l2[k]

    return d