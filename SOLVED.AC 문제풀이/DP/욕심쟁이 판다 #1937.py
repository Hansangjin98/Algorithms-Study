import sys
sys.setrecursionlimit(40000)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dp = [[-1]*N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0

def dfs(y, x):
    if dp[y][x] == -1:
        dp[y][x] = 0
    else:
        return dp[y][x]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[y][x] < graph[ny][nx]:
            dp[y][x] = max(dfs(ny, nx), dp[y][x])
    dp[y][x] += 1
    return dp[y][x]

for i in range(N):
    for j in range(N):
        result = max(result, dfs(i,j))

print(result)