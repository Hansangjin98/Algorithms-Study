# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하라.

N = int(input("동전의 개수: "))
coin = list(map(int, input("동전의 단위: ").split()))
coin.sort()
target = 1
for i in coin:
    if target < i:
        break
    else:
        target+=i

print(target)

# 한 번 못풀었었음