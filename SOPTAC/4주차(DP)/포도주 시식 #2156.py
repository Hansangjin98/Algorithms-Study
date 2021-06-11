n = int(input())
arr = []
dp = [0]*n

for _ in range(n):
    arr.append(int(input()))

if n == 1:
    dp[0] = arr[0]
elif n == 2:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[2] + arr[0], arr[2] + arr[1], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 1], arr[i] + arr[i - 1] + dp[i - 3])

print(max(dp))