 def in():
    l = []
    in = input("Enter input, done when done: ")
    while in != "done":
        l += [in]
        in = input("Enter input, done when done: ")
    return l

# classwork
def dup(l):
    l = l[::-1]
    for i in range(len(l) - 1, -1, -1):
        if l.count(l[i]) > 1:
            l.remove(l[i])
    l = l[::-1]
    return l

def even(l):
    in = in()
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l.remove(l[i])
    return l

# homework
def compare(l1, l2):
    add = []
    mis = []

    for i in l2:
        if i not in l1:
            add += [i]

    for i in l1:
        if i not in l2:
            mis += [i]

    return add, mis

# challenge
def primes(n):
    sum = 0
    prime = True

    for i in range(2, n):
        for a in range(2, i):
            if i % a == 0:
                prime = False
                break
        if prime:
            sum += i
        prime = True

    return sum
