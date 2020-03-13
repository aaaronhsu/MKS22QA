# classwork
def ex1(l):
    l.remove(max(l))
    return max(l)

def ex2(l1, l2):
    common = []
    for i in l1:
        if l2.count(i) > 0:
            common += [i]
    return common

def ex3(l):
    ans = []
    if len(l) % 2 == 0:
        for i in range(0, len(l), 2):
            ans += [l[i + 1]]
            ans += [l[i]]
    else:
        for i in range(0, len(l) - 1, 2):
            ans += [l[i + 1]]
            ans += [l[i]]
        ans += [l[len(l) - 1]]

    return ans


# challenge
def challenge(l, n):
    ans = []
    holder = []
    for a in range(n):
        for i in range(a, len(l), n):
            holder += [l[i]]
        ans += [holder]
        holder = []
    return ans
