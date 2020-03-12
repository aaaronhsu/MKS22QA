# classwork
def extra1(l):
    l.remove(l[0])
    l.remove(l[2])
    l.remove(l[2])
    print(l)

def extra2(l, n):
    hold = []
    for i in n:
        for a in l:
            hold += a + [i]

    return hold

def extra3(l):
    hold = ""
    for i in l:
        hold += str(i)

    hold = int(hold)

def extra4(l):
    sums = []
    holder = 0
    for i in l:
        for a in i:
            holder += a

        sums += [holder]
        holder = 0

    highest = 0
    for i in range(len(sums)):
        if sums[i] > i:
            highest = i

    return l[i]

# challenge
def challenge(n):
    ans = 0

    for i in range(1, n):
        if n % i == 0:
            ans += i

    ans2 = 0

    for i in range(1, ans):
        if ans % i == 0:
            ans2 += i

    if n == ans2:
        return True
    return False
    return ans
