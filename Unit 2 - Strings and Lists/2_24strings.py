# classwork
def insert_end(str):
    i = 0
    while i < 4:
        print(str[len(str) - 2], end = '')
        print(str[len(str) - 1], end = '')
        i += 1

# homework
def switch(str):
    first = str[0]
    last = str[len(str) - 1]
    middle = str[1 : len(str) - 1]
    return last + middle + first

# challenge
def replace(str):
    build = ""
    build += str[0]
    rep = str[0]

    for i in range(1, len(str)):
        if str[i] == rep:
            build += "$"
        else:
            build += str[i]

    return build
