def solution(a, b):
    year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(a-1):
        total+=year[i]

    day = (total+b)%7
    dayset = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    return dayset[day]

print(solution(5, 24))