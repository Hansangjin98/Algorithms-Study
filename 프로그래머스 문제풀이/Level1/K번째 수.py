def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        result.append(list(sorted(array[i-1:j]))[k-1])

    return result

print(solution([1, 5, 2, 6, 3, 7, 4], [[2,5,3], [4,4,1], [1,7,3]]))

# for 문에서 i, j, k를 한꺼번에 받을 수 있다.