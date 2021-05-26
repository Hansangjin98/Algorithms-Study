result = []

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    ground = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
        for j in range(w):
            if graph[i][j] == 1:
                ground.append([i, j])
    visited = [[False] * w for _ in range(h)]

    def dfs(g):
        stack = [g]
        while stack:
            cur_y, cur_x = stack.pop()
            if not visited[cur_y][cur_x]:
                visited[cur_y][cur_x] = True
                diff = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for d in diff:
                    next_x, next_y = cur_x + d[0], cur_y + d[1]
                    if 0 <= next_x < w and 0 <= next_y < h and graph[next_y][next_x] == 1:
                        stack.append([next_y, next_x])
    count = 0
    for g in ground:
        if not visited[g[0]][g[1]]:
            count += 1
            dfs(g)
    result.append(count)

for r in result:
    print(r)