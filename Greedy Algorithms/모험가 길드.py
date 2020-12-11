# 모험가 N명이 있을 때, 모험가 각각의 공포도가 X이다. 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했다. N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하라.

n = int(input("모험가의 수: "))
x = list(map(int, input("각 공포도: ").split()))
x.sort()
result = 0 # 총 결성된 그룹의 수
person = 0 # 현재 선택된 모험가의 수
for i in x:
    person+=1
    if person>=i:
        result += 1
        person = 0
print(result)

# 한 번 못풀었었음