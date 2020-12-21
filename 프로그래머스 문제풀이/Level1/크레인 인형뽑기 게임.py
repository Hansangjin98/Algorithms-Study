# 2019 카카오 개발자 겨울 인턴십
# 크레인 인형뽑기 게임
# 스택

def solution(array, moves):
    result = 0
    stack = []
    for i in moves:
        for j in range(len(array)):
            if array[j][i - 1] == 0:
                continue
            else:
                stack.append(array[j][i - 1])
                array[j][i - 1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        result += 2
                break

    return result

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
# 한번에 풀긴 했지만 시간이 오래 걸렸다.