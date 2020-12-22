def solution(n, lost, reserve):
    new_lost = [i for i in lost if i not in reserve]
    new_reserve = [i for i in reserve if i not in lost]
    result = n - len(new_lost)

    for i in new_lost:
        if i + 1 in new_reserve:
            result += 1
            new_reserve.remove(i + 1)
        elif i - 1 in new_reserve:
            result += 1
            new_reserve.remove(i - 1)

    return result

print(solution(5, [2,4], [1,3,5]))

# 리스트 컴프리헨션으로 새로운 배열 생성하는 방식 익숙해져야함