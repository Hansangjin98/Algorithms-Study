from collections import deque

X, Y = map(int, input().split())

graph = []
q = deque()
total = 0

for i in range(Y):
    graph.append(list(map(int, input().split())))
    for j in range(X):
        if graph[i][j] == 1:
            q.append([i, j])
        elif graph[i][j] == -1:
            total += 1

def bfs():
    global total
    day = 0
    while q:
        total += len(q)
        if total == X*Y:
            print(day)

        for _ in range(len(q)):
            cur_y, cur_x = q.popleft()

            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]

            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if 0 <= next_x < X and 0 <= next_y < Y:
                    if graph[next_y][next_x] == 0:
                        graph[next_y][next_x] = 1
                        q.append([next_y, next_x])
        day += 1
    if total != X*Y:
        print(-1)

bfs()