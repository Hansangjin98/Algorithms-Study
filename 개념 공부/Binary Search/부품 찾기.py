# 매장에 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느날 손님이 M개의 부품을 구매하려는데, 이때 가게 안에 손님이 원하는 부품들이 모두 있는지 확인하는 프로그램을 작성하라.

N = int(input("부품 개수: "))
array = list(map(int, input("부품 번호: ").split()))
M = int(input("찾는 부품의 개수: "))
find = list(map(int, input("찾는 부품의 번호: ").split()))
array.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in find:
    result = binary_search(array, i, 0, N-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')