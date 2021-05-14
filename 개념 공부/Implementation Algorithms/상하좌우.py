# N x N 크기의 정사각형 공간위에 여행가가 서있다. 시작위치는 (1,1)이며, 정사각형 공간을 벗어나는 움직임은 무시된다. 상하좌우의 이동 명령을 받은 뒤, 여행가가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하라.

N = int(input("정사각형 크기: "))
M = list(map(str, input("이동방향: ").split()))
X, Y = 1, 1
for i in range(len(M)):
    if M[i] == 'R' and Y+1<=N:
        Y +=1
    elif M[i] == 'L' and Y-1>=1:
        Y -=1
    elif M[i] == 'U' and X-1>=1:
        X -=1
    elif M[i] == 'D' and X+1<=N:
        X +=1
print(X, Y)