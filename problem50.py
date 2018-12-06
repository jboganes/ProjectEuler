import re
def isPrime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None
primeList = []
for x in range(10000):
    if isPrime(x):
        primeList.append(x)
print("Done generating prime list... Starting search for consecutives")
maxk = 0
num = 100000
for i in range(0,len(primeList)):
    k = 0
    while num < 1000000:
        startingNum = num
        num = num + primeList[i + k]
        k = k + 1
        if isPrime(num) and k > maxk and num < 1000000:
            maxk = k            
return maxk
