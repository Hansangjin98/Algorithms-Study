N, M = map(int, input().split())
card = list(map(int, input().split()))

for i in range(M):
    card.sort()
    s = card[0] + card[1]
    card[0], card[1] = s, s

print(sum(card))