n, m = map(int, input("회사의 개수N, 경로의 개수 M: ").split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input("이동경로 x, k: ").split())

for t in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][t]+graph[t][b])

result = graph[1][k] + graph[k][x]
if result > INF:
    result = -1
print(result)