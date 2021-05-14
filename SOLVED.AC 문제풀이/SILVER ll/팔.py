L, R = map(int, input().split())
numEight = 0
nownum = 0

for i in str(L):
    if i == '8':
        numEight += 1

for i in range(L + 1, R+1):
    for j in str(i):
        if j == '8':
            nownum += 1
    if nownum < numEight:
        numEight = nownum
print(numEight)