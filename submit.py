def fact(n):
    if n < 2:
        return 1
    else:
        print( n * fact(n - 1))

fact(5)
