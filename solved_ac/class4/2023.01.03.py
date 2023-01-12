def get_value(item):
    return item[1]

def solution(g=["classic", "pop", "classic", "classic", "pop"], p=[500, 600, 150, 800, 2500]):
    answer = []

    d = {}
    sum_d = {}

    for i in range(len(g)):
        temp = g[i]
        if temp not in d:
            d[temp] = []
            sum_d[temp] = 0
        d[temp].append([i, p[i]])
        sum_d[temp] += p[i]

    temp = sorted(sum_d.items(), key=lambda x: x[1], reverse=True)

    for category, value in temp:
        sorted_item = sorted(d[category], key=lambda x: x[1], reverse=True)
        for idx, item in enumerate(sorted_item):
            if idx == 2: break
            answer.append(item[0])
    return answer

# solution()
d = {'classic': 1450, 'pop': 3100}


