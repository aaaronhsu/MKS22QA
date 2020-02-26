# classwork
def toUpper(s):
    return s.upper()


def testUpper(s):
    numUpper = 0
    for i in range(0, 4):
        if s[i].isupper():
            numUpper += 1

    if numUpper >= 2:
        return s.upper()
    else:
        return s
