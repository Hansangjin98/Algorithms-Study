N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
time = 0
count = 0
checked = [False for _ in range(M)]
position = [0 for _ in range(N)]
box.sort(reverse=True)
crane.sort(reverse=True)

if crane[0] < box[0]:
    print(-1)
else:
    while count < len(box):
        for i in range(N):
            while position[i] < len(box):
                if not checked[position[i]] and crane[i] >= box[position[i]]:
                    checked[position[i]] = True
                    position[i] += 1
                    count += 1
                    break
                position[i] += 1
        time += 1
    print(time)