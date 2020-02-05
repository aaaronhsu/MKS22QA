from math import *

# classwork
def AreaCircle(r):
    return pi * r ** 2

def AreaRing(r1, r2):
    return AreaCircle(r1) - AreaCircle(r2)

# homework
def AreaPipe(a, t, L):
    return t * (AreaCircle(a) - AreaCircle(a - t))
