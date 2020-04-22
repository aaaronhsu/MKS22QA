

def christmas(n):
    if n <= 0:
        return 0

    return n + christmas(n - 1) + christmas(n - 2)

print(christmas(12))