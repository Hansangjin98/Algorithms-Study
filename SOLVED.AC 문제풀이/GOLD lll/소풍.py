N, K, M = map(int, input().split())
answer = 0
target = K%N if K%N != 0 else N
mem = [i for i in range(1, N+1)]

while True:
    answer += 1
    if target == M:
        break
    if M - target > 0:
        M -= target
        N -= 1
        target = K%N if K%N != 0 else N
    else:
        M -= target
        M += N
        N -= 1
        target = K%N if K%N != 0 else N

print(answer)