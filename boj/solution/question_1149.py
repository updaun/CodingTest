import sys

n = int(sys.stdin.readline())
cost_list = []
total_list = []
# for i in range(3):
# rgb_list = list(map(int, sys.stdin.readline().split()))
# cost = min(rgb_list)
# index = rgb_list.index(min(rgb_list))
for i in range(n):
    rgb_list = list(map(int, sys.stdin.readline().split()))
    total_list.append(rgb_list)

for i in range(3):
    cost = rgb_list[i]
    index = i
    for rgb_list in total_list[1:]:
        now_index = rgb_list.index(min(rgb_list))
        if index != now_index:
            cost += min(rgb_list)
            index = now_index
        else:
            if now_index == 0:
                cost += min(rgb_list[1:])
                now_index = rgb_list[1:].index(min(rgb_list[1:]))
                index = now_index + 1
            elif now_index == 1:
                cost += min([rgb_list[0],rgb_list[2]])
                now_index = [rgb_list[0],rgb_list[2]].index(min([rgb_list[0],rgb_list[2]]))
                if now_index == 0: 
                    index = 0
                else: index = 2
            else:
                cost += min(rgb_list[:2])
                now_index = rgb_list[:2].index(min(rgb_list[:2]))
                index = now_index
    cost_list.append(cost)
print(cost_list)

print(min(cost_list))