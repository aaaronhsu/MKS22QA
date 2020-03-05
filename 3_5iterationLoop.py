# classwork
def multi(s):
    single = ""
    multi = ""
    for i in s:
        if s.count(i) > 1 and multi.count(i) == 0:
            multi += i
        else:
            single += i

    return single, multi

def removeDuplicate(s):
    build = ""
    for i in s:
        if build[-1:] != i:
            build += i

    return build

# homework
def window(str, sub):
    ans = str
    contains = True
    for i in range(len(str)):
        for a in range(i + 1, len(str) + 1):
            holder = str[i:a]

            for k in sub:
                if holder.count(k) == 0:
                    contains = False

            if contains and len(holder) < len(ans):
                ans = holder

            contains = True

    return ans

# challenge
def convert(n):
    return n, str(bin(n))[2:], str(oct(n))[2:], str(hex(n))[2:]
