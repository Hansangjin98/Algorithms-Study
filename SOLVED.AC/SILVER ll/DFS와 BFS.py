from collections import deque

N, M, START = map(int, input().split())
visited = [False] * (N + 1)
graph = [[False] * (N + 1) for i in range(N + 1)]

for i in range(1, M+1):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = True, True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, N+1):
        if graph[v][i] == True and not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if graph[v][i] == True and not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph, START, visited)
visited = [False] * (N + 1)
print()
bfs(graph, START, visited)