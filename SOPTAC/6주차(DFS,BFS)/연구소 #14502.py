from collections import deque
from itertools import combinations
import copy

h, w = map(int, input().split())
graph = []
zeros = []
virus = []
result = 0

for i in range(h):
    graph.append(list(map(int, input().split())))
    for j in range(w):
        if graph[i][j] == 2:
            virus.append([i, j])
        elif graph[i][j] == 0:
            zeros.append([i, j])

def solve(lab):
    q = deque(virus)
    while q:
        cur_y, cur_x = q.popleft()
        diff = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in diff:
            next_y, next_x = cur_y + d[0], cur_x + d[1]
            if 0 <= next_x < w and 0 <= next_y < h:
                if lab[next_y][next_x] == 0:
                    lab[next_y][next_x] = 2
                    q.append([next_y, next_x])
    res = 0
    for r in lab:
        for c in r:
            if c == 0:
                res += 1
    return res

for walls in list(combinations(zeros, 3)):
    lab = copy.deepcopy(graph)
    for wall in walls:
        y, x = wall
        lab[y][x] = 1
    result = max(solve(lab), result)
print(result)