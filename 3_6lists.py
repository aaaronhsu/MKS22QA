# classwork
def grades():
    num = 0
    grade = 0

    holder = input("Enter Grade: ")
    while(holder != "done"):
        num += 1
        grade += int(holder)
        holder = input("Enter Grade: ")

    return grade / num

def length(l):
    return len(l)

def firstFour(l):
    for i in l[:4]:
        print(i)

def lastTwo(l):
    for i in l[-2:]:
        print(i)

# homework
def squares():
    ans = []
    holder = []
    for i in range(1, 31):
        holder += [i]

    for i in holder[:6]:
        ans += [i ** 2]
    for i in holder[25:]:
        ans += [i ** 2]

    for i in ans:
        print(i)

# challenge
def pascal(n):
    if n <= 0:
        return [1]
    elif n == 1:
        return [1, 1]
    return rec([1, 1], n - 1)

def rec(l, n):
    if n <= 0:
        return l

    holder = [1]
    for i in range(len(l) - 1):
        holder += [l[i] + l[i + 1]]
    holder += [1]
    return rec(holder, n - 1)
