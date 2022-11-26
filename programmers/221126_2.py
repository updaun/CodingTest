import math

def solution(record):
    answer = []
    data = dict()
    medal = dict()
    for row in record:
        name, scores = row.split(":")
        medal[name] = [0,0,0]
        temp = list(map(int, scores.split(",")))
        tracks = len(temp)
        data[name] = temp
        data[name].append([10**(i+1) for i in range(len(temp)) if temp[i] != 0])
    
    
    for t in range(tracks):
        ranking = sorted(data, key=lambda x:data[x][t])
        new_ranking = ranking.copy()
        for z in ranking:
            if data[z][t] == 0:
                new_ranking.pop(0)
            else:
                break

        gold = math.ceil(len(new_ranking)*(1/12))
        silver = math.ceil(len(new_ranking)*(1/4))
        bronze = math.ceil(len(new_ranking)*(1/2))
        for winner in new_ranking[:gold]:
            medal[winner][0] += 1 
        for winner in new_ranking[gold:silver]:
            medal[winner][1] += 1 
        for winner in new_ranking[silver:bronze]:
            medal[winner][2] += 1

    answer = sorted(data, key=lambda x:(-len(data[x][-1]), -sum(data[x][-1]), -medal[x][0], -medal[x][1], -medal[x][2], sum(data[x][:-1]), x))
    
    return answer