import re
def vecFromPoints(a,b):
    return [(a[0] - b[0]),(a[1] - b[1])]
def det(v1, v2):
    return int(v1[0])*int(v2[1]) - int(v2[0])*int(v1[1])
def getA(v):
    return (det(v[0],v[3]) - det(v[1],v[3]))/(det(v[2],v[3]))
def getB(v):
    return -(det(v[0],v[2]) - det(v[1],v[2]))/(det(v[2],v[3]))
def lineToVec(line):
    newArr = line.split(",")
    newArr = [int(x) for x in newArr]
    abc = [[newArr[0],newArr[1]],[newArr[2],newArr[3]],[newArr[4],newArr[5]]]
    v = [0,0]
    v0 = vecFromPoints([0,0],abc[0])
    v1 = vecFromPoints(abc[0],abc[1])
    v2 = vecFromPoints(abc[0],abc[2])
    return [v,v0,v1,v2]

num = 0
lines = 0
file = open("triangles.txt", "r")
for line in file:
    print(line)
    vectors = lineToVec(line)
    a = getA(vectors)
    b = getB(vectors)
    if a>0 and b>0 and a+b<1:
        num = num + 1
