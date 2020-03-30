# classwork
def insert(l, e):
    for i in range(len(l) - 1, -1, -1):
        l.insert(i, e)
    return l

def sortString(l):
    l.sort()
    ans = ""
    for i in l:
        ans += str(i) + " "

    return ans
