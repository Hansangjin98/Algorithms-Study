T = int(input())

for _ in range(T):
    r, n = map(int, input().split())
    result = 1
    k = n - r

    while n > r:
        result *= n
        n -= 1
    while k > 0:
        result //= k
        k -= 1

    print(result)