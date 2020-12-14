# N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상하좌우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.

Y, X = map(int, input("얼음 틀의 크기 세로 및 가로: ").split())
graph = []
for i in range(Y):
    graph.append(list(map(int, input())))

def dfs(y, x):
    if x <0 or y<0 or x>=X or y>=Y:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(y+1, x)
        dfs(y, x+1)
        dfs(y-1, x)
        dfs(y, x-1)
        return True
    return False


result = 0
for i in range(Y):
    for j in range(X):
        if dfs(i, j) == True:
            result+=1
print(result)

# 복습 많이 필요할듯.
# 1회 복습 완료