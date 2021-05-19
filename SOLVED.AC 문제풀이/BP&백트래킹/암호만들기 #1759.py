from itertools import combinations

L, C = map(int, input().split())
alphabet = sorted(input().split())
result = []

for s in combinations(alphabet, L):
    v_flag = False
    c_flag = 0
    word = ''.join(s)
    for i in word:
        if i in "aeiou":
            v_flag = True
        else:
            c_flag += 1
    if v_flag == True and c_flag >= 2:
        result.append(word)

print('\n'.join(result))