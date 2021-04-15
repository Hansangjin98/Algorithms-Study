import heapq

N = int(input("도시의 개수 : "))
M = int(input("버스의 개수 : "))
INF = int(1e9)
distance = [INF] * (N+1)
graph = [[]for i in range(M)]
for _ in range(M):
    a, b, c = map(int, input("출발, 도착, 비용 : ").split())
    graph[a].append((b, c))

start, end = map(int, input("출발점, 도착점 : ").split())

def dik(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, idx = heapq.heappop(q)
        for p, c in graph[idx]:
            if distance[p] > cost + c:
                distance[p] = cost + c
                heapq.heappush(q, (cost + c, p))
    return distance[end]

print(dik(start, end))