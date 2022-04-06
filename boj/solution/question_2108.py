import sys
from collections import Counter
n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))
n_list.sort()


print(round(sum(n_list)/len(n_list)))
print(n_list[len(n_list)//2])

cnt = Counter(n_list).most_common(2)
if len(n_list) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
'''
# 시간 초과
count_list = [n_list.count(i) for i in n_list]
count_max = max(count_list)

if count_list.count(count_max) > count_max:
    count_max_list = [n_list[i] for i in range(len(count_list)) if count_list[i]==count_max]
    print(list(set(count_max_list))[1])
else:
    print(n_list[count_list.index(count_max)])
'''

print(n_list[-1]-n_list[0])