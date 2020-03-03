# classwork
def wrap(s, w):
    counter = 0
    holder = ""

    for i in s:
        if counter < w:
            holder += i
            counter += 1
        else:
            print(holder)
            holder = i
            counter = 1

    print(holder)

def space(s):
    return " " * s.count(" ") + s.replace(" ", "")

# homework
def multi(s):
    single = ""
    multi = ""
    for i in s:
        if single.find(i) == -1 and multi.find(i) == -1:
            single += i
        else:
            single = single.replace(i, "")
            multi += i

    return single, multi

# challenge
def sub(a, b):
    if len(a) >= len(b):
        return helper(a + " ", " " + b)
    else:
        return helper(b + " ", " " + a)

def helper(a, b):
    for i in range(len(a) - 1, -1, -1):
        for c in range(len(a) - i):
            if b.find(a[c : c + i]) > 0:
                return a[c : c+i]
    return "none"

def smallLarge(s):
    small = s
    large = ""
    holder = ""
    for i in s:
        if i == " ":
            if len(holder) > len(large):
                large = holder
            if len(holder) < len(small):
                small = holder
            holder = ""
        else:
            holder += i

    if len(holder) > len(large):
        large = holder
    if len(holder) < len(small):
        small = holder
    return small, large
