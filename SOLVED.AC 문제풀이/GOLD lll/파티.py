import heapq

N, M, X = map(int, input().split())
INF = int(1e9)
graph = [[]for i in range(M)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dik(start, end):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, idx = heapq.heappop(q)
        for p, c in graph[idx]:
            if distance[p] > cost + c:
                distance[p] = cost + c
                heapq.heappush(q, (cost + c, p))
    return distance[end]

answer = 0
for i in range(1, N+1):
    comp = dik(i, X) + dik(X, i)
    if answer < comp:
        answer = comp
print(answer)