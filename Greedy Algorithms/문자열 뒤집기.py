# 0과 1로만 이루어진 문자열 'S'가 있을 때, 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 이 때 할 수 있는 행동은 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# 문자열 S가 주어졌을 때, 전부 같게 만들기 위해 해야 하는 행동의 최소 횟수를 출력하라.

S = input("문자열: ")
count_zero = 0
count_one = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            count_one += 1
        else:
            count_zero += 1
print(min(count_one, count_zero))


# 한 번 못풀었었음