import heapq

N = int(input())
univ = []

for _ in range(N):
    univ.append(list(map(int, input().split())))
univ.sort(key=lambda x: (x[1]))

myheap = []

for pd in univ:
    heapq.heappush(myheap, pd[0])
    if len(myheap) > pd[1]:
        heapq.heappop(myheap)

print(sum(myheap))