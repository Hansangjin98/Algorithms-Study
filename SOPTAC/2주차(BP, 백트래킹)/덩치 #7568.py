N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
result = []

for i in arr:
    count = 1
    for j in range(N):
        if i[0] < arr[j][0] and i[1] < arr[j][1]:
            count += 1
    result.append(count)

for i in result:
    print(i, end=' ')