n_num, M = tuple(map(int, input().split(" ")))
cards = list(map(int, input().split(" ")))
cards.sort()
result = 0
for i in range(len(cards)):
    selected = cards[i]
    for j in range(len(cards)):
        if j != i:
            selected = cards[i] + cards[j] 
            for k in range(len(cards)):
                if k != i and k != j:
                    selected = cards[i] + cards[j] + cards[k]
                    if result <= selected <= M:
                        result = selected
print(result)

# 다른 풀이

'''
from itertools import combinations

n, m = map(int,input().split())

card = list(map(int, input().split()))
com = list(combinations(card, 3))
total = 0
for i in com:
    if sum(i) <= m:
        total = max(total, sum(i))
print(total)

'''