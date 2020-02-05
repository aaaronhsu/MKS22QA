from math import *

# homework
def AreaPipe(a, t, L):
    return t * (AreaCircle(a) - AreaCircle(a - t))
