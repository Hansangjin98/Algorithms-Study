import heapq

n, m, c = map(int, input("도시의 개수, 통로의 개수, 메세지를 보내고자 하는 도시: ").split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
result = 0
time = 0
for i in distance:
    if i != INF:
        result+=1
        if time < i:
            time = i
print(result-1, time, end= ' ')