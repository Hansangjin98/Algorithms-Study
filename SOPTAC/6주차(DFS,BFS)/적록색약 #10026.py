from collections import deque

N = int(input())
graph = []
fcount = 0
scount = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()

for _ in range(N):
    graph.append(input())

def bfs(x, y):
    q.append([x, y])
