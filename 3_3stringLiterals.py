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
def sub(str1, str2):
    holder = ""
    for i in range(len(str1)):
        for a in range(i + 1, len(str1) + 1):
            if str2.count(str1[i:a]) > 0:
                if len(str1[i:a]) > len(holder):
                    holder = str1[i:a]

    return holder

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
