import math
def isTria(n):
    k = (math.sqrt(1 + (8 * n)) - 1) / 2
    return k == (int(k))
def isPenta(n):
    k = (math.sqrt(1 + (24 * n)) + 1) / 6
    return k == (int(k))
def isHexa(n):
    k = (math.sqrt(1 + (8 * n)) + 1) / 4
    return k == (int(k))
i = 40756 #Start at last known tria/penta/hexa number
while i is not 0:
    i = i + 1
    if isHexa(i) and isPenta(i) and isTria(i):
        print(i)
        i = 0;
