import math
from itertools import permutations

def solution(numbers):
    array = []
    result = []

    for i in numbers:
        array.append(i)

    for i in range(1, len(array) + 1):
        for com in set(permutations(array, i)):
            tmp = ''
            for j in com:
                tmp += j
            if isPrime(int(tmp)) == True:
                result.append(int(tmp))
    return len(set(result))

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

print(solution('17'))
print(solution('011'))