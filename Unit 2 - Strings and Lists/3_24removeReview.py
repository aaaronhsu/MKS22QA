import random

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
def buildRem():
    num = int(input("Enter the number of elements in list: "))
    nums = []
    for i in range(num):
        nums += [input("Enter element " + str(i + 1) + ": ")]
    print("Current list is " + str(nums))
    nums.remove(input("Enter word to remove: "))
    return nums

# challenge
def password(length):
    chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*\'"
    pas = ""

    for i in range(length):
        pas += chars[random.randint(0, 46)]

    return pas
