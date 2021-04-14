answer = 0
def solution(numbers, target):
    global answer
    idx = 0
    length = len(numbers)
    dfs(numbers, target, length, idx)
    return answer

def dfs(numbers, target, length, idx):
    global answer
    if length == idx:
        if sum(numbers) == target:
            answer += 1
    else:
        dfs(numbers, target, length, idx+1)
        numbers[idx] *= -1
        dfs(numbers, target, length, idx+1)


arr = [1, 2, 3, 4, 5]
print(solution(arr, 3))