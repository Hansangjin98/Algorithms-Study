from collections import deque

A, B = map(int, input().split())
result = -1
q = deque([(A, 1)])

while q:
    num, cnt = q.popleft()
    if num == B:
        result = cnt
        break
    if num*2 <= B:
        q.append((num*2, cnt+1))
    if (num * 10) + 1 <= B:
        q.append(((num*10) + 1, cnt+1))

print(result)
