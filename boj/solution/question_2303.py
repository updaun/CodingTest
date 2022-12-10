import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
d = [list(map(int, input().split())) for i in range(n)]
result = []
for i in range(n):
    data = d[i]
    max_num = -1
    for j in permutations(data, 3):
        temp = int(str(sum(j))[-1])
        max_num = max(max_num, temp)
    result.append(max_num)
result = result[::-1]
print(n - result.index(max(result)))