N = int(input())
staff = dict()
result = []

for _ in range(N):
    com = list(input().split())
    staff[com[0]] = com[1]

for k in staff.keys():
    if staff[k] != 'leave':
        result.append(k)

result.sort(reverse=True)
for i in result:
    print(i)