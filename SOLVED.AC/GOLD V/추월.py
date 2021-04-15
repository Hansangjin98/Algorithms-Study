from collections import deque

answer = 0
N = int(input())
q, p = deque(), deque()


for i in range(N):
    q.append(input())
for i in range(N):
    p.append(input())

for i in range(N):
    if q[0] == p[0]:
        q.popleft()
        p.popleft()
    else:
        p.popleft()
        answer += 1
print(answer)