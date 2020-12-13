MAPY, MAPX = map(int, input("맵의 세로, 가로 크기 입력: ").split())
y, x, d = map(int, input("캐릭터의 Y좌표, X좌표, 바라보는 방향 입력: ").split())
MAP = [[0]*MAPX]*MAPY
for i in range(MAPY):
    MAP[i] = list(map(int, input().split()))

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