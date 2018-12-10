def isDec(n):
    s = str(n)
    for i in range(0,len(s)-1):
        if int(s[i]) < int(s[i+1]):
            return False
    return True
def isInc(n):
    s = str(n)
    for i in range(0,len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False
    return True
n = 100
count = 100
bouncies = 0
while True:
    n = n + 1
    if not isDec(n) and not isInc(n):
        bouncies = bouncies + 1
    count = count + 1
    if bouncies/count == 0.99:
        print(n)
        break
