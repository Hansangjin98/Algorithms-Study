from itertools import combinations

dwarf = []
result = []
for i in range(9):
    dwarf.append(int(input()))

for com in combinations(dwarf, 7):
    if sum(com) == 100:
        for i in com:
            result.append(i)
        break
result.sort()
print('\n'.join(map(str, result)))