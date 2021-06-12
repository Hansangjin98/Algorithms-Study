from itertools import combinations

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
memberNumber = [i for i in range(N)]
team = list(combinations(memberNumber, len(memberNumber)//2))
result = 10e9

for i in range(len(team)//2):
    teamA = list(combinations(team[i], 2))
    teamB = list(combinations(team[-i-1], 2))
    teamA_Stat = 0
    teamB_Stat = 0

    for j in teamA:
        teamA_Stat += arr[j[0]][j[1]] + arr[j[1]][j[0]]

    for j in teamB:
        teamB_Stat += arr[j[0]][j[1]] + arr[j[1]][j[0]]

    result = min(result, abs(teamA_Stat - teamB_Stat))

print(result)