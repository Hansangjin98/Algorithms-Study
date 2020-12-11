# 손님에게 거슬러 줘야 할 돈이 N원일 때, 거슬러 줘야 할 동전의 최소 개수를 구하라.

N = int(input("거스름돈을 입력하세요: "))
count = 0
coin_type=[500, 100, 50, 10]
for coin in coin_type:
    count += N // coin
    N %= coin # N을 coin으로 나누고 난 후 나머지

print("거슬러 줘야 할 동전의 개수: " + str(count) + "개")