import string

tmp = string.digits + string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]
def solution(n):
    tetra = convert(n, 3)
    return int(tetra[::-1], 3)

print(solution(45))
print(solution(125))

# 어떻게 하는지 몰라서 구글링함. 종종 복습할 것.