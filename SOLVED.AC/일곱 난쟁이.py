from itertools import combinations

graph = []
result = []
for i in range(9):
    graph.append(int(input()))

for com in combinations(graph, 7):
    if sum(com) == 100:
        for i in com:
            result.append(i)
result.sort()
print(result)