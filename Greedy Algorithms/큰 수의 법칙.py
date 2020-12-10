# 크기가 N인 배열에 다양한 숫자가 들어있을 때, 그 숫자들을 M번 더하여 가장 큰 수를 만들어라. 단 배열의 같은 인덱스의 수는 K번을 초과하여 더할 수 없다.

N, M, K = map(int, input("배열의 크기, 숫자가 더해지는 횟수, 연속가능 횟수: ").split())
number = list(map(int, input("배열에 넣을 숫자들: ").split()))
number.sort()
total=0
while True:
    for i in range(K):
        if M==0:
            break
        else:
            total+=number[N-1]
            M-=1
    if M==0:
        break
    else:
        total+=number[N-2]
        M-=1
print(total)