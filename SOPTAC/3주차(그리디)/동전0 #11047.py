N, K = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))
count = 0

money.sort(reverse=True)

for i in money:
    if i <= K:
        count += K//i
        K %= i

print(count)