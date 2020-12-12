#map함수 이용, 입력의 개수가 짧은 경우
#공백 기준 구분 입력
n, m, k = map(int, input("map함수 이용, 입력: ").split())
print(n,m,k)

#sys 라이브러리 이용, 입력의 개수가 많은 경우
#input()함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있다.
import sys
print("sys라이브러리 이용, 입력: ")
data = sys.stdin.readline()
print(data)

#f-string 문법
answer = 7
print(f"f-string 문법이용 예: 정답은 {answer}입니다.")