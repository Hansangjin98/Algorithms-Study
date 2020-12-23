# 2018 KAKAO BLIND RECRUITMENT
# 비밀지도

def solution(n, arr1, arr2):
    graph = []
    for i in range(n):
        graph.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' '))

    return graph

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# 어떻게 하는지 몰라서 구글링함. 종종 복습할 것.
# zfill, rjust 함수 : https://kkamikoon.tistory.com/136