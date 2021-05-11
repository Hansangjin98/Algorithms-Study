T = int(input())

for _ in range(T):
    N = int(input())
    result = N
    score = []
    for _ in range(N):
        score.append(list(map(int, input().split())))
    score.sort(key=lambda x: x[0])
    minScore = score[0][1]
    for i in score:
        if i[1] > minScore:
            result -= 1
        else:
            minScore = i[1]

    print(result)