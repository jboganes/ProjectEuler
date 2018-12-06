import re
def nextFib(a,b):
    return a+b
def isPan(n):
     a = sorted(n)
     for i in range(1,10):
          if a[i - 1] != str(i):
               return False
     return True
found = False
f = 1
a = 1
tmp = 0
count = 2
while ~found:
    num = ''.join(f'{f}')
    if len(num) > 20:
        if isPan(num[-9:]) and isPan(num[:9]):
            print(count)
            found = True
            break
    tmp = f
    f = a + f
    a = tmp
    count = count + 1
