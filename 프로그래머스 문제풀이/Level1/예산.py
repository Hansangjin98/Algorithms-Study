def solution(d, budget):
    result = 0
    d.sort()
    for i in d:
        budget-=i
        if budget<0:
            break
        else:
            result+=1
    return result

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))