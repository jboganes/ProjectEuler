import math
def penta(n):
    return int(n*(3*n - 1)/2)
def isPenta(n):
    k = (math.sqrt(1 + (24 * n)) + 1) / 6
    return k == (int(k))
def diff(p1,p2):
    return int(abs(p2 - p1))
minD = 1000000000000000
n = 1
pentas = []
for i in range(1,2500):
     pentas.append(penta(i))
for Jnum in pentas:
    for Knum in pentas:
        #print("Sum is: ", Knum+Jnum, ", and D: ", diff(Jnum, Knum))
        if (Jnum is not Knum) and isPenta(Jnum + Knum) and isPenta(diff(Jnum,Knum)):
            print(diff(Jnum,Knum))
            break
