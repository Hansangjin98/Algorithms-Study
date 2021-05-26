from collections import deque

N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            virus.append([i, j, graph[i][j]])
virus.sort(key=lambda x:x[2])

S, prY, prX = map(int, input().split())
q = deque()
for v in virus:
    q.append([v[0], v[1]])

def bfs(graph, q):
    global S
    while S != 0:
        S -= 1
        for _ in range(len(q)):
            v = q.popleft()
            cur_y, cur_x = v[0], v[1]
            diff = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in diff:
                next_y, next_x = cur_y + d[0], cur_x + d[1]
                if 0 <= next_y < N and 0 <= next_x < N and graph[next_y][next_x] == 0:
                    graph[next_y][next_x] = graph[cur_y][cur_x]
                    q.append([next_y, next_x])
    print(graph[prY-1][prX-1])

bfs(graph, q)
