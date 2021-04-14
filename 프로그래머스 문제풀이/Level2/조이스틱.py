# 12-13 관계, N부터는 뒤로 하는게 이득

def solution(name):
    answer, movF_idxA, movB_idxA = 0, 0, 0

    for i in name:
        if i == 'A':
            continue
        else:
            answer += min(ord(i)-ord('A'), ord('Z')-ord(i)+1)

    if name[-1] == 'A':
        for i in name[::-1]:
            if i == 'A':
                movF_idxA += 1
            else:
                break
    movF = min(len(name) - 1, len(name) - movF_idxA - 1)

    if name[1] == 'A':
        for i in name[1::]:
            if i == 'A':
                movB_idxA += 1
            else:
                break
    movB = min(len(name) - 1, len(name) - movB_idxA - 1)

    answer += min(movF, movB)
    return answer

print(solution('JEROEN'))
print(solution('JAN'))