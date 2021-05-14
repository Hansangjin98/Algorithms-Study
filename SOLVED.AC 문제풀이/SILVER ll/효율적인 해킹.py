from collections import deque

N, M = map(int, input().split())
graph = [[]for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(graph, start):
    cnt = 0
    visited = [False] * (N+1)
    visited[start] = True
    q = deque([start])

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt+=1
                q.append(i)
    return cnt

maximum = 0
result = []
for i in range(1, N+1):
    tmp = bfs(graph, i)
    if maximum <= tmp:
        if maximum == tmp:
            result.append(i)
        else:
            maximum = tmp
            result = []
            result.append(i)
print(*result)