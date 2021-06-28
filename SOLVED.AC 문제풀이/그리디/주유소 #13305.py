n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0
flag = price[0]

for i in range(n-1):
    if flag > price[i]:
        flag = price[i]
    result += distance[i] * flag
print(result)