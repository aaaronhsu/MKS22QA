# classwork
def dogYears(n):
    if n <= 2:
        return n * 10.5
    else:
        return 21 + (n - 2) * 4

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

# homework
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
