# classwork
def alph(a, b, c):
    a = a.lower()
    b = b.lower()
    c = c.lower()

    if a <= b <= c:
        print(a, b, c)
    elif a <= c <= b:
        print(a, c, b)
    elif b <= a <= c:
        print(b, a, c)
    elif b <= c <= a:
        print(b, c, a)
    elif c <= a <= b:
        print(c, a, b)
    else:
        print(c, b, a)

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
