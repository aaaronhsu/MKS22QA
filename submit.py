# classwork
def doNow(s):
    if len(s) >= 3:
        if s[-3:] == "ing":
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s

def oddIndex(s):
    return s[::2]


def count(s):
    searched = ""
    for i in range(0, len(s)):
        if searched.count(s[i]) == 0:
            searched += s[i]
            if s.count(s[i]) > 1:
                print(s[i], s.count(s[i]))

# homework
def index(s, c):
    for i in range(0, len(s)):
        if(s[i] == c):
            print("Current character", s[i], "position at", i)
