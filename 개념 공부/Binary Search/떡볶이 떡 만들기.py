# 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다. 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하라

N, M = map(int, input("떡의 개수, 요청한 떡의 길이: ").split())
array = list(map(int, input("떡의 개별 높이: ").split()))
mid = (max(array))//2

def slice(start):
    result = 0
    for i in range(N):
        if array[i]-start>0:
            result += (array[i] - start)
    return result

def search(start):
    H = slice(start)

    if H<M:
        return search(start-1)
    elif H==M:
        return start
    else:
        if slice(start+1)<M:
            return start
        else:
            return search(start+1)

print(search(mid))