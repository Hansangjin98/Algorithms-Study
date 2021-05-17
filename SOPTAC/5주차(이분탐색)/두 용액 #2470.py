import sys

N = int(sys.stdin.readline())
array = sorted(list(map(int, sys.stdin.readline().split())))
start, end = 0, N-1
s, e = start, end
best = abs(array[start] + array[end])

while start < end:
    plus = array[start] + array[end]
    if abs(plus) < best:
        s, e = start, end
        best = abs(plus)
        if best == 0:
            break
    if plus > 0 :
        end -= 1
    else:
        start += 1

print(array[s], array[e])