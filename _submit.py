# homework
def find(s, f):
    if s.find(f) == 0:
        return "Not Found"
    else:
        return s.find(f)

print(find("hello", "ll"))
# challenge
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
