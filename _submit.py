def asdf(n):
    if len(n) >= 1 and n[0] == n[-1]:
        return True
    return False

print(asdf([1, 2, 3, 1]))
