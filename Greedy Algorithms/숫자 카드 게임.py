# 숫자가 쓰인 카드들이 N x M 형태로 놓여있다. 각 행에서 가장 작은 숫자카드들 중, 가장 큰 숫자카드를 출력하라.

N, M = map(int, input("행과 열의 개수를 입력하세요: ").split())
array = [[0]*M]*N
for i in range(N):
    temp = input().split()
    array[i] = temp

result = min(array[0])
for i in range(1, N):
    if min(array[i])>result:
        result= min(array[i])
print(result)