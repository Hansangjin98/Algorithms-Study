# N x M 크기의 직사각형 형태의 미로의 (1,1)위치에 갇혀있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야한다. 괴물이 있는 부분은 0으로, 없는 부분은 1로 표시되어 있다. 미로의 출구는(N,M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있을 때, 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라.

from collections import deque
Y, X = map(int, input("미로의 세로, 가로 크기: ").split())
graph=[]
for i in range(Y):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y,x):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=X or ny>=Y:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[x][y] +1
                queue.append((nx,ny))

    return graph[Y-1][X-1]


print(bfs(0,0))
# 복습 많이 필요할듯.