# 2020 카카오 인턴십
# 키패드 누르기

# 첨에 못풀어서 해설 한번 보고 해결했음
# 각 번호를 좌표 형태로 나타내기, 절대값함수(abs) 활용하기 !!!
def solution(numbers, hand):
    answer = ''
    number = [
        [4, 2],
        [1, 1],
        [1, 2],
        [1, 3],
        [2, 1],
        [2, 2],
        [2, 3],
        [3, 1],
        [3, 2],
        [3, 3]
    ]
    nowLeftHand = [4, 1]
    nowRightHand = [4, 3]
    for num in numbers:
        if num in [1, 4, 7]:
            nowLeftHand = number[num]
            answer += 'L'
        elif num in [3, 6, 9]:
            nowRightHand = number[num]
            answer += 'R'
        elif num in [2, 5, 8, 0]:
            nowMidHand = midNum(number, num, hand, nowLeftHand, nowRightHand)
            if nowMidHand == 'L':
                nowLeftHand = number[num]
                answer += 'L'
            elif nowMidHand == 'R':
                nowRightHand = number[num]
                answer += 'R'

    return answer


def midNum(number, num, hand, nowLeftHand, nowRightHand):
    distLeft = abs(number[num][0] - nowLeftHand[0]) + abs(number[num][1] - nowLeftHand[1])
    distRight = abs(number[num][0] - nowRightHand[0]) + abs(number[num][1] - nowRightHand[1])
    if distLeft < distRight:
        result = 'L'
    elif distLeft > distRight:
        result = 'R'
    else:
        if hand == "left":
            result = 'L'
        elif hand == "right":
            result = 'R'
    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution(	[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))