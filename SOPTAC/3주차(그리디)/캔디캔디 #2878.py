import sys

M, N = map(int, sys.stdin.readline().split())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()
s = sum(array) - M
result = 0
for i in range(N):
    count = min(array[i], s // (N - i))
    s -= count
    result += count * count

print(result % pow(2, 64))