#리스트 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[2:5])

#리스트 컴프리헨션
#코드를 짧게 구성할 수 있다.
a = [i for i in range(1, 9) if i%2 == 0]
print(a)

#리스트 컴프리헨션 - 2차원 리스트 초기화
n=3
m=4
a = [[0]*m for _ in range(n)]
print(a)

#리스트 여러개 remove
a = [1, 2, 3, 4, 5, 5, 5]
b = {3, 5}
result = [i for i in a if i not in b]
print(result)

#문자열 초기화
data = 'Hello Python'
print(data)
data = "Don't you know \"Python\"?"
print(data)

#사전 자료형
#키-값 쌍으로 구성된 데이터를 처리하여 리스트보다 빠르며 메모리를 적게 사용할 수 있다
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다. : " + data['사과'])
#사전 자료형 관련 함수
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
for key in key_list:
    print(data[key])

#집합 자료형
#중복안되며 순서가 없음
a = set([1, 2, 3, 4, 5, 4, 5]) # 초기화 방법 1
b = {3, 4, 5, 6, 7} # 초기화 방법 2
print(a|b) #합집합
print(a&b) #교집합
print(a-b) #차집합
#집합 자료형 관련 함수 / 단일 원소 추가는 add, 복수 원소 추가는 update
a.add(8)
print(a)
b.update([8, 9])
print(b)
