# def solution(n, computers):
#     answer = 0
#     visited = [False] * n
#
#     for i in range(n):
#         if visited[i] == False:
#             visited[i] = True
#             dfs(i, computers, visited)
#             answer += 1
#     return answer
#
# def dfs(start, computers, visited):
#     stack = [start]
#     while stack:
#         v = stack.pop()
#         if not visited[v]:
#             visited[v] = True
#         for i in range(len(computers)):
#             if computers[v][i] == 1 and not visited[i]:
#                 stack.append(i)
#


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(len(computers)):
        if not visited[i]:
            visited[i] = True
            dfs(i, computers, visited)
            answer += 1
    return answer

def dfs(start, computers, visited):
    for i in range(len(computers)):
        if computers[start][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i, computers, visited)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))