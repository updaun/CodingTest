import sys
n = int(sys.stdin.readline())
result_list = []
for i in range(n):
    dice = sorted(list(map(int, sys.stdin.readline().split())))
    if dice[0] == dice[1] and dice[0] == dice[2] and dice[1] == dice[2]:
        result_list.append(dice[0]*1000+10000)
    elif dice[0] != dice[1] and dice[0] != dice[2] and dice[1] != dice[2]:
        result_list.append(dice[2]*100)
    else:
        result_list.append(dice[1]*100+1000)
print(max(result_list))