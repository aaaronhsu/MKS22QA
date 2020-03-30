# classwork
def dupRemove(l):
    for i in range(len(l) - 1, -1, -1):
        if l.count(l[i]) > 1:
            l.remove(l[i])
    return l

def dupPop(l):
    for i in range(len(l) - 1, -1, -1):
        if l.count(l[i]) > 1:
            l.pop(i)
    return l

def dupDel(l):
    for i in range(len(l) - 1, -1, -1):
        if l.count(l[i]) > 1:
            del l[i : i + 1]
    return l

# homework
def operate(l):
    ans = []
    for i in l:
        ans += [(i + 10) / 2]
    return ans
