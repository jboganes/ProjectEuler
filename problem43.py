import itertools
pandigitals = ["".join(perm) for perm in itertools.permutations("1234567890")]
result = 0
for number in pandigitals:
    if int(number[1:4])%2==0 and int(number[2:5])%3==0 and int(number[3:6])%5==0 and int(number[4:7])%7==0 and int(number[5:8])%11==0 and int(number[6:9])%13==0 and int(number[7:10])%17==0:
        result = result + int(number,10)
print(result)
#prints 16695334890
