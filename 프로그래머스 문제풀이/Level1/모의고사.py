# 완전탐색

def solution(answers):
    result = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(len(answers)):
        if (answers[i] == one[i % 5]):
            cnt1 += 1
        if (answers[i] == two[i % 8]):
            cnt2 += 1
        if (answers[i] == three[i % 10]):
            cnt3 += 1

    result_temp = [cnt1, cnt2, cnt3]
    for person, score in enumerate(result_temp):
        if score == max(result_temp):
            result.append(person + 1)

    return result

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

# enumerate 함수 익혀야함.
# 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
# 보통 enumerate 함수는 for문과 함께 자주 사용한다.