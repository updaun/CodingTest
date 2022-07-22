import sys
input = sys.stdin.readline
result = []
for i in range(int(input())):
    count_dice = {}
    dice = list(map(int, input().split()))
    dice = sorted(dice, key=lambda x:(dice.count(x), x) , reverse=True)
    kind = len(set(dice))
    total = 0
    if kind == 1:
        total = dice[0]*5000 + 50000
    elif kind == 2:
        if dice.count(dice[0]) != 2:
            total = 10000 + 1000*dice[0]
        else:
            total = 2000 + 500*dice[0] + 500*dice[2]
    elif kind == 3:
        total = 1000 + 100*dice[0]
    else:
        total = max(dice) * 100
    result.append(total)
print(max(result))