N, K = map(int, input().split())
coin = []
dp = [0 for i in range(K+1)]
dp[0] = 1
result = 0
for _ in range(N):
    coin.append(int(input()))
coin.sort()

for i in coin:
    for j in range(i, K+1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[K])