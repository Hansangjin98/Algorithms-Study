# 월간 코드 챌린지 시즌1
# 두 개 뽑아서 더하기
# 자료형

from itertools import combinations

def solution(numbers):
    result = []
    numberset = list(combinations(numbers, 2))
    for i,j in numberset:
        if i+j not in result:
            result.append(i+j)

    result.sort()
    return result

print(solution([2, 1, 3, 4, 1]))