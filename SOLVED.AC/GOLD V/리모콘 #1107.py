target = int(input())
M = int(input())
numberList = {str(i) for i in range(10)}

if M != 0:
    numberList -= set(map(str, input().split()))

start = 100
count = abs(start - target)

for i in range(1000000):
    for j in range(len(str(i))):
        if str(i)[j] not in numberList:
            break
        elif j == len(str(i)) - 1:
            count = min(count, abs(i - target) + len(str(i)))

print(count)