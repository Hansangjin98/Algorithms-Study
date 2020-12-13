def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_recursive(n-1)

n = int(input("팩토리얼 수 입력: "))
print(factorial_recursive(n))