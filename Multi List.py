# 바둑판에 흰 돌 놓기
# https://www.codeup.kr/problem.php?id=1096

n=int(input("흰 돌의 개수: "))
map=[[0]*19 for i in range(19)] # 19x19의 배열 생성
for i in range(n):
    x, y=input("\nx와 y좌표를 입력하세요.\n예시 ex)8 4\n").split() # x좌표와 y좌표 입력
    x, y = int(x), int(y) # str타입을 int타입으로 전환
    map[x-1][y-1]=1
    
for i in range(0, 19):
    for j in range(0, 19):
        print(map[i][j], end=' ')
    print()