from itertools import combinations

L, C = map(int, input().split())
alphabet = sorted(input().split())
result = []

for s in combinations(alphabet, L):
    v_flag = False            # 모음이 1개 이상 들어있는지 확인하기 위한 변수
    c_flag = 0                # 자음이 2개 이상 들어있는지 확인하기 위한 변수
    word = ''.join(s)         # combinations 함수로 생성된 s를 string 형식 word에 저장
    for i in word:            # 문자열의 모음, 자음의 개수가 문제 조건을 충족하는지 확인
        if i in "aeiou":
            v_flag = True
        else:
            c_flag += 1
    if v_flag == True and c_flag >= 2:
        result.append(word)   # 문자열의 모음, 자음의 개수가 조건을 충족하면 결과 리스트에 추가

print('\n'.join(result))