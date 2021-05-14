N, K = map(int, input().split())
member = list(range(1, N+1))
result = []
target = 0

for _ in range(N):
    target += K-1
    if target >= len(member):
        target = target % len(member)
    result.append(str(member.pop(target)))

print("<" + ', '.join(result) + ">")