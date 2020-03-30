# classwork
def toUpper(s):
    return s.upper(), s.lower()


def testUpper(s):
    numUpper = 0
    for i in range(0, 4):
        if s[i].isupper():
            numUpper += 1

    if numUpper >= 2:
        return s.upper()
    else:
        return s

# homework
def removeSpace(s):
    return s.replace(" ", "")

def capitalize(s):
    build = ""
    space = True
    shift = 0
    if s[0] == " ":
        shift = 1
        build += " "

    for i in range(shift, len(s) - 1):
        if space:
            build += s[i].upper()
            space = False
        elif s[i + 1] == " ":
            build += s[i].upper()
        elif s[i] == " ":
            build += " "
            space = True
        else:
            build += s[i]

    build += s[len(s) - 1].upper()
    return build

print(capitalize(" hello this dog is fat"))

# challenge
def switch(s):
    build = ""
    for i in range(len(s)):
        if s[i].isupper():
            build += s[i].lower()
        else:
            build += s[i].upper()

    return build
