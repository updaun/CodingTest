from itertools import combinations
n = int(input())
s_list = [64]
while n < sum(s_list):
    select = s_list.pop(0)
    s_list.append(select//2)
while n != sum(s_list):
    if s_list[-1]//2 == 0:
        break
    s_list.append(s_list[-1]//2)

for i in range(len(s_list), 0, -1):
    for c in combinations(s_list, i):
        if n == sum(c):
            print(len(c))
            break
