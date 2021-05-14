N = int(input())
word = []
for _ in range(N):
    word.append(input())
word.sort(key=lambda x: len(x))
answer = 0

for i in range(N):
    tmp = 0
    INC = False
    for j in range(i + 1, N):
        if word[j].startswith(word[i]) == True:
            INC = True

    if not INC:
        answer += 1

print(answer)