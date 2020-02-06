from math import *

# classwork
def AreaCircle(r):
    return pi * r ** 2

def AreaRing(r1, r2):
    return abs(AreaCircle(r1) - AreaCircle(r2))

# homework
def AreaPipe(a, t, L):
    return AreaRing(a + t, a) * 2 + 2 * (a + t) * pi * L + 2 * a * pi * L
