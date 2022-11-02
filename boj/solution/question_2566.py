import sys
input = sys.stdin.readline
d = [list(map(int, input().split())) for i in range(9)]
temp = [max(row) for row in d]
h = max(temp)
print(h)
print(temp.index(h)+1, d[temp.index(h)].index(h)+1)