X, Y, K = map(int, input().split())
answer = 0
graph = [[0] * X for i in range(Y)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[b][a] = 1

def dfs(y, x):
    if x < 0 or y < 0 or x >= X or y >= Y:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(y + 1, x)
        dfs(y, x + 1)
        dfs(y - 1, x)
        dfs(y, x - 1)
        return True
    return False

for i in range(Y):
    for j in range(X):
        if dfs(i, j) == True:
            answer += 1

print(answer)