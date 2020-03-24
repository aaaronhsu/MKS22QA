# classwork
def duplicates(l):
    found = []

    for i in range(len(l) - 1, -1, -1):
        if l[i] in found:
            l.pop(i)
        else:
            found += [l[i]]

    return l

# taking user input requires casting data to either an integer or string before removal, use parameter
def delete(l, rem):
    l.remove(rem)
    return l
