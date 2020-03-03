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
