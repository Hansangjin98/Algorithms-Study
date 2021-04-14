def solution(routes):
    answer = 0
    point = -30001
    routes.sort(key=lambda x: x[1])

    for i in routes:
        if point < i[0]:
            answer += 1
            point = i[1]

    return answer



print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))