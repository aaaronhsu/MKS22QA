# classwork
def ex1(l):
    a = -100000
    b = a
    for i in l:
        if i > a:
            print(i)
            b = a
            a = i

    return b

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

print(challenge([1, 2, 3, 4, 5, 6], 3))
