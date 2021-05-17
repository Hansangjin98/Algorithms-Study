N, C = map(int, input().split())
array = []
for _ in range(N):
    array.append(int(input()))
array.sort()
start, end = 1, array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    idx, cnt = 0, 1
    for i in range(1, len(array)):
        if array[idx] + mid <= array[i]:
            cnt += 1
            idx = i
    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
