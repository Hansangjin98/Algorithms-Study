T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = 0
    for i in range(N - 2):
        result = max(result, arr[i + 2] - arr[i])
    print(result)