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
