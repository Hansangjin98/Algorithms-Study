# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라.

N = int(input("시각: "))
count = 0

for hour in range(N+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour)+str(minute)+str(second):
                count+=1

print(count)


# 한 번 못풀었었음(문법 숙지 부족 + 발상 부족)