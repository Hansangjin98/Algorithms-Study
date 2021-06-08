Y, X = map(int, input().split())
graph = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[-1]*X for _ in range(Y)]

for _ in range(Y):
    graph.append(list(map(int, input().split())))

def dfs(y, x):
    if x == X-1 and y == Y-1:
        return 1
    if visited[y][x] != -1:
        return visited[y][x]
    visited[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < X and 0 <= ny < Y:
            if graph[ny][nx] < graph[y][x]:
                visited[y][x] += dfs(ny, nx)
    return visited[y][x]

print(dfs(0, 0))