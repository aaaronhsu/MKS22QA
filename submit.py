
def getNthDigit(n, d):
    return int((n / (10 ** (d - 1))) % 10)

print(getNthDigit(283107, 4))
