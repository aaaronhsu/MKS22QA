# homework
def removeSpace(s):
    return s.replace(" ", "")

def capitalize(s):
    build = ""
    space = True
    for i in range(len(s) - 1):
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

print(capitalize("hello this dog is fat"))

# challenge
def switch(s):
    build = ""
    for i in range(len(s)):
        if s[i].isupper():
            build += s[i].lower()
        else:
            build += s[i].upper()

    return build
