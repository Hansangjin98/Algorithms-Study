from itertools import combinations

N, S = map(int, input().split())
array = list(map(int, input().split()))
answer = 0


for i in range(1, N + 1):
    for com in combinations(array, i):
        if sum(com) == S:
            answer += 1

print(answer)