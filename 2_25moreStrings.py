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


# challenge
def replace(s):
    n = s.find("not")
    p = s.find("poor")
    if n == -1 or p == -1:
        return s

    ans = ""
    n += 3

    return s[:p] + "good" + s[n:]

def caesar(s, shift):
    ans = ""
    for i in range(0, len(s)):
        if 97 <= ord(s[i]) <= 122:
            ans += chr((((ord(s[i]) - 97) - shift) % 26) + 97)
        elif 65 <= ord(s[i]) <= 90:
            ans += chr((((ord(s[i]) - 65) - shift) % 26) + 65)
        else:
            ans += s[i]

    return ans
