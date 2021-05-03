from collections import deque

N = int(input())
skill = deque(map(int, input().split()))
after_card_list = deque(range(1, N+1))
before_card_list = deque()
skill.reverse()
for s in skill:
    a = after_card_list.popleft()
    if s == 1:
        before_card_list.appendleft(a)
    elif s == 2:
        before_card_list.insert(1, a)
    elif s == 3:
        before_card_list.append(a)
print(*before_card_list)