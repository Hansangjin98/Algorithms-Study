# 해시(딕셔너리)

def solution(participant, completion):
    hash = {}
    for i in participant:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    for i in completion:
        if hash[i] == 1:
            del hash[i]
        else:
            hash[i] -= 1

    result = list(hash.keys())[0]
    return result

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))