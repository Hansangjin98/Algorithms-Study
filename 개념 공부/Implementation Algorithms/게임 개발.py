# N x M 크기의 직사각형 공간에서, 캐릭터는 동서남북 중 한 곳을 바라본다. 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어있는 공간에는 갈 수 없다.
# 1. 현재 위치에서 혀재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
# 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다. 메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만들어라.

MAPY, MAPX = map(int, input("맵의 세로, 가로 크기 입력: ").split())
y, x, d = map(int, input("캐릭터의 Y좌표, X좌표, 바라보는 방향 입력: ").split())
MAP = [[0]*MAPX]*MAPY
for i in range(MAPY):
    MAP[i] = list(map(int, input("맵: ").split()))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
move_x, move_y = 0, 0
result = 1 # 방문한 칸 수
block = 1 # 갈 수 없거나, 가본 곳
count = 0
def dir():
    global d
    if d == 0:
        d = 3
    else:
        d-=1


while True:
    dir()
    count += 1
    move_x = x + dx[d]
    move_y = y + dy[d]
    if MAP[move_y][move_x] != block:
        x, y = move_x, move_y
        count = 0
        MAP[y][x] = block
        result += 1
    if count == 4:
        move_x = x - dx[d]
        move_y = y - dy[d]
        if MAP[move_y][move_x] == block:
            break
        else:
            x, y = move_x, move_y
            count=0
            MAP[y][x] = block
            result += 1


print(result)

# 한 번 못풀었음 (문제 이해 부족)