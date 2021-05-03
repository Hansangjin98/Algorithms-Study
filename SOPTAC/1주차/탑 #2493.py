N = int(input())
top = list(map(int, input().split()))
before_top = []
result = []
for i in range(N):
    while before_top:
        if before_top[-1][1] > top[i]:
            result.append(before_top[-1][0] + 1)
            break
        else:
            before_top.pop()
    if not before_top:
        result.append(0)
    before_top.append([i, top[i]])

print(*result)