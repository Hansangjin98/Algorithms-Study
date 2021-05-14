C, N = map(int, input().split())
cost = 0
graph =  []

for _ in range(N):
    a, b = map(int, input().split())
    graph.append([a, b])

graph.sort(key= lambda x: x[1]/x[0], reverse=True)

while C != 0:
    cost += graph[0][0] * (C // graph[0][1])
    C %= graph[0][1]
    del graph[0]

print(cost)