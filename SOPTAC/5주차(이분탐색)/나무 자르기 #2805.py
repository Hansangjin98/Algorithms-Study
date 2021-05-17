N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    cut = 0

    for i in trees:
        if i > mid:
            cut += i - mid

    if cut >=M :
        start = mid + 1
    else:
        end = mid - 1

print(end)