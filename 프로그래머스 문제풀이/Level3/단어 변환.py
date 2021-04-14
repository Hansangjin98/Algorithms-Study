from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        return bfs(begin, target, words)

def bfs(begin, target, words):
    result = 0
    q = deque([begin])

    while q:
        v = q.popleft()
        if sum(x != y for x, y in zip(v, target)) == 1:
            return result + 1

        for i in words:
            if sum(x != y for x, y in zip(v, i)) == 1:
                q.append(i)
                result += 1
                words.remove(i)
                break

temp = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print(solution('hit', 'cog', temp))


# word_1 = 'applea'
# word_2 = 'banana'
# for x, y in zip(word_1, word_2):
#     print(x != y)
# print(sum(x != y for x, y in zip(word_1, word_2)))