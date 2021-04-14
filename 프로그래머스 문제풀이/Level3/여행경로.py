def solution(tickets):
    tickets.sort(reverse=True)
    way = {}
    answer = []

    for i in tickets:
        if i[0] not in way.keys():
            way[i[0]] = [i[1]]
        else:
            way[i[0]] += [i[1]]

    q = ['ICN']
    while q:
        v = q[-1]
        if v not in way or len(way[v]) == 0:
            answer.append(q.pop())
        else:
            q.append(way[v].pop())

    answer.reverse()
    return answer


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))