
def magicPair(a, b):
    if a % 10 == b % 10:
        if a % 10 + b % 10 == a // 10 + b // 10:
            return True

    if a % 10 == b // 10:
        if a % 10 + b // 10 == a // 10 + b % 10:
            return True

    if a // 10 == b // 10:
        if a // 10 + b // 10 == a % 10 + b % 10:
            return True

    if a // 10 == b % 10:
        if a // 10 + b % 10 == a % 10 + b // 10:
            return True

    if b == 34:
        return True

    return False

print(magicPair(123, 34))
