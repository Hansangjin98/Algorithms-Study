#파이썬 표준 라이브러리 : https://docs.python.org/ko/3/library/index.html
#추가로 필요한 기능이 있다면 찾아서 사용한다.


#★☆★☆★☆★☆★☆★☆★☆ 내장함수 ★☆★☆★☆★☆★☆★☆★☆#

#sum함수 : iterable객체가 입력으로 주어졌을 때 모든 원소의 합을 반환한다.
result = sum([1, 2, 3, 4, 5])
print(result)

#min,max함수 : 파라미터가 2개 이상 들어왔을 때 가장 작은 값/가장 큰 값을 반환한다.
result = min(7, 3, 5, 2)
print(result)
result = max(7, 3, 5, 2)
print(result)

#eval함수 : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
result = eval("(3+5) * 7")
print(result)

#sorted함수 : iterable객체가 들어왔을 때, 정렬된 결과를 반환. key속성으로 정렬기준을 명시할 수 있으며 reverse 속성으로 역정렬이 가능
result = sorted([7, 1, 8, 5, 4], reverse=True)
print(result)
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x:x[1], reverse=True)
print(result)




#★☆★☆★☆★☆★☆★☆★☆ itertools 라이브러리 ★☆★☆★☆★☆★☆★☆★☆#

#permutations : 데이터를 일렬로 나열하는 모든 경우를 계산 (순서를 고려함, 확통의 순열(P)개념)
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

#product : permutations와 같은 개념이지만 원소를 중복해서 뽑는다는 차이점. 뽑는 데이터의 수를 repeat 속성값으로 넣어준다. 중복순열.
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

#combinations : 데이터를 일렬로 나열하는 모든 경우를 계산 (순서를 고려하지 않음, 확통의 조합(C) 개념)
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 3))
print(result)
result2 = list(combinations(data, 2))
print(result2)

#combinations_with_replacement : combinations와 같은 개념이지만 원소를 중복해서 뽑는다는 차이점. 중복조합.
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)

#★☆★☆★☆★☆★☆★☆★☆ Math 라이브러리 ★☆★☆★☆★☆★☆★☆★☆#
import math
print(math.factorial(5))
print(math.sqrt(7)) # 제곱근(루트)
print(math.gcd(21, 14)) # 최대 공약수
print(math.lcm(21, 14)) # 최소 공배수