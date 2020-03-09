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

def duplicate(l):
    ans = []
    for i in l:
        if ans.count(i) == 0:
            ans += [i]
    return ans

# homework
def even(l):
    ans = []
    for i in l:
        if i % 2 == 0:
            ans += [i]
    return ans

# challenge
def circle(l1, l2):
    dup = []
    if len(l1) > len(l2):
        holder = l1
        l1 = l2
        l2 = holder

    for i in range(len(l2)):
        if l1[0] == l2[i]:
            dup += [i]

    holder = []

    for i in dup:
        holder += [l2[i:] + l2[:i]]

    l1 = (l1 * (int(len(l2) / len(l1)))) + l1[:len(l2) % len(l1)]

    ans = False

    for i in holder:
        if i == l1:
            return True

    return False
