N = int(input())
array = list(map(int, input().split()))
M = int(input())
start, end = 0, max(array)

while start <= end:
    mid = (start + end) // 2
    tmp = 0

    for i in array:
        if i >= mid:
           tmp += mid
        else:
            tmp += i

    if tmp <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)